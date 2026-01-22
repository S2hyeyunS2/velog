<h3 id="database-낙관적-락optimistic-lock--비관적-락pessimistic-lock"> 낙관적 락(Optimistic Lock) &amp; 비관적 락(Pessimistic Lock)</h3>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span>
<strong>낙관적 락</strong>은 “충돌이 드물다” 가정하고 <strong>UPDATE 시점에 버전으로 검증</strong>하며, <strong>비관적 락</strong>은 “충돌이 많다” 가정하고 <strong>DB 락(S/X)로 먼저 막는다.</strong></p>
</blockquote>
<p>트랜잭션이 동시에 같은 데이터를 수정하면 <strong>갱신 분실(Lost Update)</strong>, <strong>경쟁 조건(Race Condition)</strong> 같은 문제가 생길 수 있다.
이를 해결하기 위해 크게 두 가지 접근이 있다.</p>
<ul>
<li><strong>낙관적 락(Optimistic Lock)</strong>: <em>일단 락 없이 진행 → 마지막에 충돌 여부 확인</em></li>
<li><strong>비관적 락(Pessimistic Lock)</strong>: <em>처음부터 락을 잡고 진행 → 다른 트랜잭션 접근 차단</em></li>
</ul>
<hr />
<h3 id="낙관적-락optimistic-lock">낙관적 락(Optimistic Lock)</h3>
<blockquote>
<p><strong>읽을 때 락 없음</strong>
<strong>수정(UPDATE) 시점에 “내가 읽은 이후로 바뀌었는지” 검증</strong></p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>데이터를 읽을 때는 락을 걸지 않아서 <strong>읽기 성능/동시성</strong>이 유리할 수 있음</li>
<li>보통 <code>version</code> 같은 <strong>별도 컬럼(버전 필드)</strong> 로 변경 여부를 확인</li>
<li>충돌 발생 시 DB가 자동으로 해결해주지 않기 때문에
→ <strong>애플리케이션에서 재시도/실패 처리</strong>가 필요함</li>
</ul>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>충돌이 “드물다”는 전제</strong></span>에서 가장 효율적이다.
예) 조회가 많고 수정이 상대적으로 적은 서비스, 사용자별로 다른 데이터 갱신 등</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">동작 흐름</span></p>
<ol>
<li>데이터 조회 시 <code>version</code>도 함께 조회</li>
<li>수정 시 <code>WHERE id=? AND version=?</code> 조건으로 업데이트</li>
<li>업데이트 결과가 0건이면 → 이미 다른 트랜잭션이 수정함(충돌)
→ 재시도 또는 예외 처리</li>
</ol>
<p><span style="background-color: #f6f8fa;">SQL 예시</span></p>
<pre><code class="language-sql">-- 1) 읽기
SELECT id, value, version
FROM table_name
WHERE id = 1;

-- 2) 수정(버전 체크)
UPDATE table_name
SET value = 'new', version = version + 1
WHERE id = 1 AND version = 3;</code></pre>
<details>
<span style="background-color: #f5f0ff;">🔎 포인트 (왜 “락이 없다”고 하나?)</span>

<p>낙관적 락은 보통 <strong>DB의 S/X 락을 적극적으로 잡는 방식이 아니라</strong>,
버전 컬럼으로 <strong>충돌을 “검출”</strong> 하는 전략이다.
그래서 충돌 처리는 DB가 아니라 <strong>애플리케이션 레벨(재시도/롤백)</strong> 에서 진행되는 경우가 많다.</p>
</details>

<hr />
<h3 id="비관적-락pessimistic-lock">비관적 락(Pessimistic Lock)</h3>
<blockquote>
<p><strong>트랜잭션 중간에 충돌이 날 가능성이 크다</strong>
그래서 <strong>S/X 락을 먼저 확보</strong>하여 다른 트랜잭션 접근을 제한한다</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>특정 row(또는 범위)에 대해 <strong>공유락(S)</strong> 또는 <strong>배타락(X)</strong> 을 획득</li>
<li>다른 트랜잭션은 락이 풀릴 때까지 <strong>대기(Wait)</strong> 할 수 있음</li>
<li>충돌을 “나중에 해결”이 아니라 <strong>애초에 막는 방식</strong>이라 로직이 단순해질 수 있음</li>
</ul>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>충돌이 “자주” 나는 데이터</strong></span>에서 유리할 수 있다.
예) 재고 차감, 잔액 차감, 쿠폰 사용, 좌석 예약처럼 <strong>동일 row를 여러 요청이 동시에 갱신</strong>하는 경우</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">SQL 예시</span></p>
<pre><code class="language-sql">-- 배타락(X) 확보: 다른 트랜잭션의 수정/락 획득을 막음
SELECT * FROM table_name WHERE id = 1 FOR UPDATE;

-- (조건 검사 후)
UPDATE table_name SET value = 'new' WHERE id = 1;</code></pre>
<details>
<span style="background-color: #f5f0ff;">🔎 참고 (S/X 락과의 관계)</span>

<p>비관적 락은 DB가 제공하는 <strong>공유락(S) / 배타락(X)</strong> 같은 락 메커니즘을 적극 활용한다.
즉, “비관적 락 = DB 락 기반으로 충돌을 미리 차단”에 가깝다.</p>
</details>

<hr />
<h3 id="두-방식의-차이점-핵심만">두 방식의 차이점 (핵심만)</h3>
<ol>
<li><strong>충돌 처리 방식</strong></li>
</ol>
<ul>
<li><span style="background-color: #fff5b1;">낙관적 락</span>: 충돌이 나면 <strong>그때 감지 → 재시도/실패 처리</strong></li>
<li><span style="background-color: #fff5b1;">비관적 락</span>: 충돌이 나기 전에 <strong>락으로 미리 차단</strong></li>
</ul>
<ol start="2">
<li><strong>DB 락 사용 여부</strong></li>
</ol>
<ul>
<li>낙관적 락: 보통 <strong>S/X 락을 거의 쓰지 않음</strong>(버전 체크 중심)</li>
<li>비관적 락: <strong>S/X 락을 사용</strong>(FOR UPDATE 등)</li>
</ul>
<ol start="3">
<li><strong>성능/운영 포인트</strong></li>
</ol>
<ul>
<li>낙관적 락: 평소 빠를 수 있지만, 충돌 잦으면 <strong>재시도 비용</strong>이 커짐</li>
<li>비관적 락: 충돌은 줄지만, 락 대기로 <strong>지연/병목</strong>이 생길 수 있음</li>
</ul>
<hr />
<h3 id="어떤-락을-언제-쓰면-좋을까">어떤 락을 언제 쓰면 좋을까?</h3>
<blockquote>
<p>💡 정답은 “뭐가 더 좋은가?”가 아니라 <strong>충돌 빈도와 요구사항</strong>이다.</p>
</blockquote>
<p><span style="background-color: #d1ebf9;"><strong>낙관적 락이 유리한 경우</strong></span></p>
<ul>
<li>조회가 많고 수정 충돌이 드문 경우</li>
<li>실패/재시도 처리를 애플리케이션에서 수용 가능할 때</li>
<li>사용자 단위로 분산된 데이터 업데이트(동일 row 경쟁이 적음)</li>
</ul>
<p><span style="background-color: #d1ebf9;"><strong>비관적 락이 유리한 경우</strong></span></p>
<ul>
<li>동일 row에 대한 수정 경쟁이 잦은 경우(재고/잔액/예약)</li>
<li>“한 번에 정확히” 처리되어야 하는 무결성 요구가 강한 경우</li>
<li>재시도 로직을 복잡하게 가져가고 싶지 않을 때(대신 대기/타임아웃 관리 필요)</li>
</ul>
<hr />
<h3 id="한눈에-정리">한눈에 정리</h3>
<ul>
<li><span style="background-color: #fff5b1;"><code>낙관적 락</code></span> : 락 없이 진행 → <strong>UPDATE 시점 충돌 검증(version)</strong> → 재시도/실패 처리</li>
<li><span style="background-color: #fff5b1;"><code>비관적 락</code></span> : <strong>DB 락(S/X)</strong> 을 먼저 잡아서 → 충돌 자체를 차단(대기 발생 가능)</li>
</ul>