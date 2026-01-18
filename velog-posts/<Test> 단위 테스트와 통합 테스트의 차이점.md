<h3 id="test-단위-테스트와-통합-테스트의-차이점">[Test] 단위 테스트와 통합 테스트의 차이점</h3>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span>
** 단위 테스트는 소프트웨어의 가장 작은 단위를 대상<strong>으로 개별 단위의 동작을 검증 
**통합 테스트는 여러 단위가 함께 잘 작동하는지 확인</strong>하는데 초점을 둠 </p>
</blockquote>
<ul>
<li>단위 테스트는 개발 초기에 수행되어 개별 단위의 버그를 빠르게 발견하고 수정할 수 있게 함.</li>
<li>통합 테스트는 개발의 후반 단계에서 수행되며, 시스템의 전체적인 동작을 검증함.</li>
</ul>
<hr />
<h3 id="test의-중요성">Test의 중요성</h3>
<ul>
<li>테스트를 통해 개발된 소프트웨어가 요구사항을 만족하는지, 버그 없이 잘 동작하는지 확인할 수 있음</li>
<li>테스트 없이는 소프트웨어의 품질을 보장할 수 없고, 사용자의 신뢰를 떨어뜨릴 수 있음</li>
<li>소프트웨어는 여러 기능이 럭혀 동작하기 때문에 작은 변경 하나가 전체 오류로 이어질 수 있음</li>
</ul>
<p>이를 방지하기 위해 <span style="background-color: #fff5b1;"><strong>테스트는 코드가 의도한 대로 동작하는지</strong></span>를 지속적으로 검증하는 수단</p>
<hr />
<h3 id="test-종류">Test 종류</h3>
<h4 id="1-단위테스트">1) 단위테스트</h4>
<blockquote>
<p>단위테스트는 소프트웨어의 가장 작은 단위
개별 메서드나 함수의 기능을 검증하는 테스트
특정 기능이 올바르게 동작하는지 확인하기 위해 독립적이고 빠르게 실행</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>개발자가 직접 작성</li>
<li>JUnit, PyTest 등의 테스트 프레임워크 사용</li>
<li>실행 속도가 빠름</li>
<li>DB, 네트워크 등 외부 의존성은 Mock 처리</li>
</ul>
<p><span style="background-color: #f6f8fa;">장점</span></p>
<ul>
<li>개발 초기 단계에서 버그를 빠르게 발견 가능</li>
<li>리팩토링 및 기능 추가 시 안정성 확보</li>
<li>버그 발생 시 원인 파악이 쉬움</li>
</ul>
<p><span style="background-color: #f6f8fa;">예시</span></p>
<pre><code class="language-java">@Test
void sumTest() {
    assertEquals(5, sum(2, 3));
}</code></pre>
<hr />
<h4 id="2-통합테스트">2) 통합테스트</h4>
<blockquote>
<p>개별 모듈들이 결합되어 전체 시스템이 올바르게 동작하는지 검증
모듈 간의 상호작용이 올바르게 동작하는지 확인
실제 데이터베이스, 네트워크 등의 외부 시스템과의 통합을 테스트</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">특징</span></p>
<ul>
<li>여러 모듈을 함께 테스트</li>
<li>실제 DB, 네트워크, 외부 API와 연동</li>
<li>단위 테스트보다 실행 시간이 김</li>
<li>환경 설정이 비교적 복잡함</li>
</ul>
<p><span style="background-color: #f6f8fa;">예시</span></p>
<pre><code class="language-java">@SpringBootTest
class OrderIntegrationTest {

    @Test
    void orderFlowTest() {
        // 주문 → 결제 → 저장 흐름 검증
    }
}</code></pre>
<hr />
<h3 id="단위-테스트-vs-통합-테스트-차이점">단위 테스트 vs 통합 테스트 차이점</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>단위 테스트</th>
<th>통합 테스트</th>
</tr>
</thead>
<tbody><tr>
<td>테스트 대상</td>
<td>함수, 메서드</td>
<td>여러 모듈</td>
</tr>
<tr>
<td>실행 시점</td>
<td>개발 초기</td>
<td>개발 후반</td>
</tr>
<tr>
<td>실행 속도</td>
<td>매우 빠름</td>
<td>비교적 느림</td>
</tr>
<tr>
<td>목적</td>
<td>개별 로직 검증</td>
<td>전체 흐름 검증</td>
</tr>
<tr>
<td>외부 의존성</td>
<td>Mock 처리</td>
<td>실제 연동</td>
</tr>
</tbody></table>
<hr />
<h3 id="오해-정리">오해 정리</h3>
<p><span style="background-color: #ffdce0;"><strong>오해 1</strong></span>
“단위 테스트만 있으면 충분하다”
→ 단위 테스트는 모듈 간 연결 오류를 검증하지 못한다</p>
<p><span style="background-color: #ffdce0;"><strong>오해 2</strong></span>
“통합 테스트는 단위 테스트를 대체한다”
→ 통합 테스트는 문제 원인 추적이 어렵다</p>
<hr />
<h3 id="한눈에-정리">한눈에 정리</h3>
<p><span style="background-color: #fff5b1;"><strong>단위 테스트</strong></span> : 빠른 피드백, 안정적인 코드 변경
<span style="background-color: #fff5b1;"><strong>통합 테스트</strong></span> : 실제 시스템 동작 검증</p>
<p>두 테스트는 대체 관계가 아닌 보완 관계</p>