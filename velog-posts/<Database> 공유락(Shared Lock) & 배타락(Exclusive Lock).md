<h3 id="database-공유락shared-lock--배타락exclusive-lock"> 공유락(Shared Lock) &amp; 배타락(Exclusive Lock)</h3>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span>
트랜잭션이 동시에 실행될 때 생기는 충돌을 막기 위해 DBMS는 <strong>Lock(락)</strong> 을 사용하고, 대표적으로 <strong>공유락(S)</strong> 과 <strong>배타락(X)</strong> 이 있다.</p>
</blockquote>
<p>트랜잭션을 <strong>특별한 제어 없이 병행 수행</strong>하도록 두면, 데이터의 <strong>일관성 / 무결성</strong>을 보장하기 어려울 수 있다.
이때 병행 트랜잭션을 제어하기 위해 DBMS는 <code>Lock(락)</code> 을 사용하며, 기본적으로 <code>공유락(Shared, S)</code> 과 <code>배타락(Exclusive, X)</code> 로 나뉜다.</p>
<hr />
<h3 id="lock이란">Lock이란?</h3>
<blockquote>
<p>트랜잭션이 접근한 데이터에 대해 <strong>다른 트랜잭션의 접근을 제한</strong>하여
<strong>동시성(Concurrency)을 제어</strong>하는 메커니즘이다.</p>
</blockquote>
<hr />
<h3 id="lock-종류-s--x">Lock 종류 (S / X)</h3>
<h4 id="1-shared-lock-공유락-s">1) Shared Lock (공유락, S)</h4>
<blockquote>
<p> <strong>읽기(SELECT) 가능 / 쓰기 불가</strong>
<strong>다른 트랜잭션의 배타락(X) 획득을 막는다</strong></p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>다른 트랜잭션의 <strong>공유락(S)</strong> 은 허용</li>
<li>다른 트랜잭션의 <strong>배타락(X)</strong> 은 허용하지 않음</li>
<li>결과적으로 공유락을 잡고 있는 동안 해당 데이터는 <strong>다른 트랜잭션이 수정하지 못하게</strong> 할 수 있음
→ “내가 읽은 값이 중간에 바뀌는 상황”을 방지</li>
</ul>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>읽은 값이 트랜잭션이 끝날 때까지 바뀌면 안 되는 상황</strong></span>에서 사용한다.
예) “재고가 5개 이상이면 주문 승인” 판단 중 다른 트랜잭션이 재고를 줄이면 판단이 틀어질 수 있음</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">SQL 예시</span></p>
<pre><code class="language-sql">SELECT * FROM table_name WHERE id = 1 FOR SHARE;</code></pre>
<details>
<span style="background-color: #f5f0ff;">🔎 참고 (MVCC)</span>

<p>DBMS에 따라 일반 SELECT는 MVCC로 “락 없이” 읽히는 경우가 많다.
따라서 공유락은 보통 <strong>명시적으로 잠그는 읽기</strong>에서 등장한다.</p>
</details>

<hr />
<h4 id="2-exclusive-lock-배타락-x">2) Exclusive Lock (배타락, X)</h4>
<blockquote>
<p><strong>다른 트랜잭션의 S/X 락 획득을 모두 차단</strong>
즉, 다른 트랜잭션이 <code>공유락/배타락</code>을 <strong>둘 다 얻지 못하게</strong> 막는다</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>배타락이 걸린 데이터는 다른 트랜잭션이 <strong>공유락(S), 배타락(X)</strong> 을 모두 획득할 수 없음</li>
<li>배타락을 획득한 트랜잭션은 해당 데이터를 <strong>독점적으로 변경</strong>할 수 있음</li>
<li>다만, <strong>락을 얻지 않는 일반 SELECT</strong>가 읽히는지 여부는 <strong>DBMS(MVCC) / 격리수준</strong>에 따라 달라질 수 있음</li>
</ul>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>내가 수정할 데이터를 다른 트랜잭션이 건드리지 못하게</strong></span> 해야 할 때 사용한다.</p>
<ul>
<li><code>UPDATE / DELETE</code> 같은 <strong>쓰기 작업 자체</strong></li>
<li>“읽기 → 조건 확인 → 수정” 사이에 경쟁 조건을 막아야 할 때
예) 잔액 확인 후 차감 / 쿠폰 사용 처리 / 좌석 예약 / 주문 상태 전이</li>
</ul>
</blockquote>
<p><span style="background-color: #f6f8fa;">SQL 예시</span></p>
<pre><code class="language-sql">SELECT * FROM table_name WHERE id = 1 FOR UPDATE;</code></pre>
<hr />
<h3 id="배타락에-대한-오해-정리">배타락에 대한 오해 정리</h3>
<blockquote>
<p> <span style="background-color: #ffdce0;"><strong>오해 1</strong></span>
 “배타락은 읽기/쓰기 둘 다 절대 불가능”
정확히는 <strong>다른 트랜잭션의 공유락(S) / 배타락(X) 획득을 막는다</strong>가 맞다.</p>
</blockquote>
<blockquote>
<p><span style="background-color: #ffdce0;"><strong>오해 2</strong></span><br />“배타락이면 무조건 SELECT도 안 된다”
<code>락을 얻지 않는 일반 SELECT</code>는 <strong>DBMS(MVCC) / 격리수준</strong>에 따라 읽힐 수도, 막힐 수도 있다.</p>
</blockquote>
<hr />
<h3 id="한눈에-정리">한눈에 정리</h3>
<ul>
<li><span style="background-color: #fff5b1;"><code>공유락(S)</code></span> : 여러 트랜잭션의 <strong>동시 읽기 허용</strong>, <strong>수정(X) 차단</strong></li>
<li><span style="background-color: #fff5b1;"><code>배타락(X)</code></span> : 다른 트랜잭션의 <strong>S/X 모두 차단</strong> → <strong>대기 발생 가능</strong></li>
<li>락 충돌이 생기면 트랜잭션은 락이 해제될 때까지 <strong>대기(Wait)</strong> 할 수 있다.</li>
</ul>
<hr />
<h3 id="deadlock교착상태">Deadlock(교착상태)</h3>
<blockquote>
<p>⚠️ <span style="background-color: #F7DDBE;"><strong>데드락</strong></span>
두 개 이상의 트랜잭션이 서로가 가진 락이 풀리길 기다리며 <strong>무한 대기</strong>에 빠지는 현상</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">예시 시나리오</span></p>
<ul>
<li>트랜잭션 A, B가 존재</li>
<li>데이터 <code>id=1</code>, <code>id=2</code>가 존재</li>
<li>A는 <code>id=1</code>을 먼저 잡고 → <code>id=2</code> 변경 시도</li>
<li>B는 <code>id=2</code>를 먼저 잡고 → <code>id=1</code> 변경 시도</li>
</ul>
<p><span style="background-color: #f6f8fa;">발생 흐름</span></p>
<ol>
<li>A가 <code>id=1</code> 락 획득</li>
<li>B가 <code>id=2</code> 락 획득</li>
<li>A는 <code>id=2</code>가 필요하지만 B가 잡고 있어 <strong>대기</strong></li>
<li>B는 <code>id=1</code>이 필요하지만 A가 잡고 있어 <strong>대기</strong></li>
<li>서로 기다리기만 하며 진행 불가 → <strong>Deadlock</strong></li>
</ol>
<blockquote>
<p>대부분의 DBMS는 데드락을 감지하면 한 트랜잭션을 롤백(희생자 선택)하여 교착 상태를 해소한다.</p>
</blockquote>
<hr />
<h3 id="데드락을-줄이는-방법">데드락을 줄이는 방법</h3>
<blockquote>
<p> <span style="background-color: #d1ebf9;"><strong>1) 락 획득 순서를 일관되게</strong></span>
모든 트랜잭션이 항상 같은 순서로 자원을 잠그도록 설계한다.
예) 항상 <code>id=1 → id=2</code> 순서로 락 획득</p>
</blockquote>
<blockquote>
<p><span style="background-color: #d1ebf9;"><strong>2) 락 타임아웃 설정</strong></span>
일정 시간 이상 대기하면 실패 처리(롤백)로 빠져나오게 해서 시스템 정체를 완화한다.</p>
</blockquote>