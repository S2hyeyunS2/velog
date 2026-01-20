<h2 id="performance-tuning-cache-vs-message-queuemq"> Cache vs Message Queue(MQ)</h2>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span>
트래픽 폭주로 서버가 느려졌다면 “Redis가 빠르니까 캐시”, “Kafka가 핫하니까 MQ”가 아니라, <strong>병목이 읽기(Read)인지 쓰기/처리(Write)인지부터</strong> 나눠서 선택해야 한다.</p>
</blockquote>
<p>트래픽이 폭주해서 서버가 느려졌을 때 면접에서 자주 나오는 질문이 있다.</p>
<blockquote>
<p>“캐시(Cache)와 메시지 큐(MQ) 중 무엇을 도입하시겠습니까?”</p>
</blockquote>
<p>많이들 아래처럼 생각하기 쉬운데,</p>
<ul>
<li>Redis가 빠르니까 캐시를 쓰겠다</li>
<li>Kafka가 핫하니까 MQ를 도입하겠다</li>
</ul>
<p><span style="background-color: #ffdce0;"><strong>오해</strong></span>
사실 <strong>정답은 “병목이 어디에서 생기냐”</strong>에 따라 달라진다.
즉, <strong>읽기가 문제인지(Read)</strong>, <strong>쓰기가 문제인지(Write)</strong> 를 먼저 구분해야 한다.</p>
<hr />
<h3 id="cache란-읽기-최적화">Cache란? (읽기 최적화)</h3>
<blockquote>
<p>자주 조회되는 데이터/계산 결과를 <strong>빠른 저장소(주로 메모리)</strong> 에 보관해두고 <strong>재사용(Reuse)</strong> 하여 <strong>DB 접근을 줄이는 방식</strong></p>
</blockquote>
<h4 id="span-stylebackground-colorf6f8fa예시span"><span style="background-color: #f6f8fa;">예시</span></h4>
<ul>
<li>주문이 들어올 때마다 요리(DB 조회/계산)하는 대신
<strong>미리 만들어둔 결과를 0.1초 만에 제공</strong>하는 느낌</li>
</ul>
<hr />
<h3 id="message-queuemq란-쓰기처리-최적화">Message Queue(MQ)란? (쓰기/처리 최적화)</h3>
<blockquote>
<p>요청을 즉시 끝까지 처리하지 않고 <strong>대기열(Queue)</strong> 에 넣어두고,
<strong>Worker가 비동기(Async)</strong> 로 처리하여 <strong>부하를 분산</strong>하고 <strong>결합도를 낮추는 방식</strong></p>
</blockquote>
<h4 id="span-stylebackground-colorf6f8fa예시span-1"><span style="background-color: #f6f8fa;">예시</span></h4>
<ul>
<li>주문(요청)은 <strong>일단 접수</strong>하고 즉시 응답</li>
<li>요리(처리)는 <strong>주방(Worker) 사정에 맞춰</strong> 천천히 처리</li>
</ul>
<hr />
<h3 id="시스템-구조-어디에-배치되는가">시스템 구조 (어디에 배치되는가?)</h3>
<h4 id="1-read-path-cache">1) Read Path (Cache)</h4>
<ul>
<li><strong>User → Cache(Redis) → DB</strong></li>
<li><em>DB 앞단에서 부하를 막아줌</em></li>
</ul>
<h4 id="2-write-path-mq">2) Write Path (MQ)</h4>
<ul>
<li><strong>User → API Server → MQ(Kafka) → Worker/DB</strong></li>
<li><em>로직 처리의 비동기화(Async) / 버퍼링</em></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/0aacf0a1-50fa-49b3-9973-80149b0d39b4/image.png" /></p>
<hr />
<h3 id="언제-무엇을-쓸까">언제 무엇을 쓸까?</h3>
<blockquote>
<p>핵심은 “느려진 이유”가 <strong>조회(Select)</strong> 때문인지, <strong>처리/쓰기(Insert/Update)</strong> 때문인지다.</p>
</blockquote>
<h4 id="cache를-쓰면-좋은-경우">Cache를 쓰면 좋은 경우</h4>
<ul>
<li>조회(SELECT) 쿼리가 너무 많아서 <strong>DB가 느릴 때</strong></li>
<li>동일 데이터/동일 계산 결과 요청이 반복될 때
→ <strong>결과를 저장해두고 DB 접근을 줄이기</strong></li>
</ul>
<h4 id="mq를-쓰면-좋은-경우">MQ를 쓰면 좋은 경우</h4>
<ul>
<li>주문/결제처럼 <strong>복잡한 로직(Insert/Update + 외부 연동 + 무거운 작업)</strong> 때문에 느릴 때
→ <strong>일단 접수하고, 처리는 나중에(비동기)</strong> + <strong>부하 조절(Throttling)</strong></li>
</ul>
<p><span style="background-color: #d1ebf9;"><strong>선택 팁</strong></span>
DB CPU/쿼리 폭증이면 Cache, 요청 처리시간/백엔드 작업 적체면 MQ 쪽을 먼저 의심한다.</p>
<hr />
<h3 id="cache-전략-look-aside">Cache 전략: Look Aside</h3>
<blockquote>
<p>앱이 “필요할 때만” 캐시를 채우는 가장 흔한 패턴</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">동작 흐름</span></p>
<ol>
<li>데이터가 캐시에 있는지 확인(Look)</li>
<li>있으면(Hit) → 바로 반환</li>
<li>없으면(Miss) → DB 조회 → 캐시에 저장(Aside) → 반환</li>
</ol>
<hr />
<h3 id="mq-전략-async-worker">MQ 전략: Async Worker</h3>
<blockquote>
<p>API는 빠르게 응답하고, 무거운 처리는 Worker에게 넘긴다</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">동작 흐름</span></p>
<ol>
<li>클라이언트 요청을 받으면 MQ에 넣고 <strong>바로 응답</strong></li>
<li>백그라운드 Worker가 MQ에서 메시지를 하나씩 꺼냄</li>
<li>무거운 작업(이메일 발송, 썸네일 생성 등)을 <strong>순차 처리</strong></li>
</ol>
<p>→ 시스템 과부하를 막고(Throttling) 결합도를 낮춤</p>
<hr />
<h3 id="도입-전-고려사항">도입 전 고려사항</h3>
<h4 id="cache-고려사항">Cache 고려사항</h4>
<ul>
<li><span style="background-color: #fff5b1;"><strong>데이터 정합성</strong></span>: DB와 캐시 값이 달라질 수 있음</li>
<li><span style="background-color: #fff5b1;"><strong>관리 비용</strong></span>: TTL(만료), 갱신/무효화 정책 필요</li>
</ul>
<h4 id="mq-고려사항">MQ 고려사항</h4>
<ul>
<li><span style="background-color: #fff5b1;"><strong>복잡도 증가</strong></span>: 비동기라 장애/재시도/중복 처리 설계가 필요</li>
<li><span style="background-color: #fff5b1;"><strong>실시간성</strong></span>: 큐가 밀리면 사용자는 결과를 늦게 받음</li>
</ul>
<hr />
<h3 id="모범-답안">모범 답안</h3>
<blockquote>
<p>우선 모니터링을 통해 병목 지점이 <strong>읽기(Read)인지 쓰기/처리(Write)인지</strong> 파악하겠습니다.
조회 쿼리 부하가 원인이라면 <strong>Redis 캐시</strong>로 DB 부하를 줄이고,
처리 지연/복잡한 로직이 원인이라면 <strong>Kafka(MQ)</strong> 로 비동기 전환하여 부하를 조절하겠습니다.</p>
</blockquote>