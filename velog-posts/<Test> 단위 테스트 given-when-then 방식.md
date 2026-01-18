<h3 id="test-방식">Test 방식</h3>
<p>요즘 Java에서 단위 테스트를 작성할 때는 주로 <span style="background-color: #fff5b1;"><strong>JUnit5 + AssertJ</strong></span> 조합이 사용된다.</p>
<hr />
<h3 id="junit-assertj-이란">JUnit, AssertJ 이란?</h3>
<blockquote>
<p><span style="background-color: #f6f8fa;"><strong>JUnit5</strong></span><br />자바 <strong>단위 테스트를 작성하고 실행하기 위한 테스팅 프레임워크</strong></p>
</blockquote>
<blockquote>
<p><span style="background-color: #f6f8fa;"><strong>AssertJ</strong></span><br />테스트 결과를 <strong>더 읽기 쉬운 문법으로 검증</strong>할 수 있도록 도와주는 라이브러리</p>
</blockquote>
<p>JUnit만으로도 단위 테스트 작성은 충분히 가능하다.<br />하지만 <code>assertEquals()</code> 와 같은 기본 assertion 메서드는 조건이 많아질수록 <strong>가독성이 떨어진다</strong>는 단점이 있다.</p>
<p>이 때문에 순수 Java 애플리케이션에서는 <span style="background-color: #fff5b1;"><strong>JUnit5와 AssertJ를 함께 사용</strong></span>하여 테스트 의도를 더 명확하게 표현하는 방식이 많이 사용된다.</p>
<hr />
<h3 id="given-when-then-패턴">given/ when/ then 패턴</h3>
<blockquote>
<p>하나의 단위 테스트를 <strong>준비 → 실행 → 검증</strong>   세 단계로 나누어 작성하는 테스트 패턴</p>
</blockquote>
<ul>
<li><p><span style="background-color: #f6f8fa;">given (준비)</span><br />테스트에 필요한 데이터와 환경을 준비</p>
</li>
<li><p><span style="background-color: #f6f8fa;">when (실행)</span><br />테스트하려는 메서드나 기능을 실행</p>
</li>
<li><p><span style="background-color: #f6f8fa;">then (검증)</span><br />실행 결과가 기대한 값과 일치하는지 검증</p>
</li>
</ul>
<p>이 패턴을 사용하면 <strong>테스트 코드의 흐름이 자연스럽게 읽히고</strong>, 무엇을 검증하는 테스트인지 한눈에 파악할 수 있다.</p>
<hr />
<h3 id="test-code-예시">Test code 예시</h3>
<p>스파르타 심화과정 마지막 프로젝트인 이커머스 payment-service 개발 과정에서 단위 테스트를 작성하며 given / when / then 패턴을 적용했다.</p>
<p><span style="background-color: #f6f8fa;">예시 (payment-service 일부 발췌)</span></p>
<pre><code class="language-java">@Test
void 결제가_정상적으로_완료된다() {
    // given: 결제 정보 준비
    Payment payment = new Payment(10000);
    PaymentService paymentService = new PaymentService();

    // when: 결제 실행
    PaymentResult result = paymentService.pay(payment);

    // then: 결과 검증
    assertThat(result.isSuccess()).isTrue();
    assertThat(result.getAmount()).isEqualTo(10000);
}</code></pre>
<hr />
<h3 id="마무리">마무리</h3>
<blockquote>
<p>JUnit5와 AssertJ를 함께 사용하고 <strong>given / when / then 패턴</strong>을 적용하면 테스트 의도를 명확하게 드러내는 단위 테스트를 작성할 수 있다.</p>
</blockquote>