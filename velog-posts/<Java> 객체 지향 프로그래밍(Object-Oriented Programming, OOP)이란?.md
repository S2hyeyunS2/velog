<h3 id="java-객체-지향-프로그래밍object-oriented-programming-oop"> 객체 지향 프로그래밍(Object-Oriented Programming, OOP)</h3>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span>
OOP는 <strong>상태(필드)와 행위(메서드)를 가진 객체</strong>를 중심으로, <strong>역할/책임을 나눠 협력</strong>하며 프로그램을 설계하는 패러다임이다.</p>
</blockquote>
<p>객체 지향 프로그래밍(OOP)은 데이터를 뜻하는 <strong>상태(필드)</strong> 와 동작을 뜻하는 <strong>행위(메서드)</strong> 를 하나의 단위(객체)로 묶어 설계한다.
각 객체에 <strong>역할(Role)</strong> 과 <strong>책임(Responsibility)</strong> 을 부여하고, 객체들이 <strong>메시지로 협력</strong>하면서 전체 시스템을 구성한다.</p>
<hr />
<h4 id="oop의-특징-4가지">OOP의 특징 4가지</h4>
<ul>
<li><span style="background-color: #fff5b1;"><strong>캡슐화(Encapsulation)</strong></span> : 상태/행위를 하나로 묶고, 내부 구현을 숨기며 인터페이스만 노출</li>
<li><span style="background-color: #fff5b1;"><strong>추상화(Abstraction)</strong></span> : 핵심만 남기고 세부 구현은 감추어 공통 개념을 정의</li>
<li><span style="background-color: #fff5b1;"><strong>다형성(Polymorphism)</strong></span> : 같은 인터페이스가 다양한 형태로 동작(오버로딩/오버라이딩)</li>
<li><span style="background-color: #fff5b1;"><strong>상속(Inheritance)</strong></span> : 상위 특성을 하위가 물려받아 확장(재사용/중복 제거)</li>
</ul>
<hr />
<h4 id="1-encapsulation-캡슐화">1) Encapsulation (캡슐화)</h4>
<blockquote>
<p><strong>상태 + 행위를 하나로 묶고, 외부에는 필요한 인터페이스만 제공</strong>
내부 구현을 숨겨 <strong>무결성 보호</strong> + <strong>유지보수성 향상</strong></p>
</blockquote>
<p><span style="background-color: #f6f8fa;">핵심 포인트</span></p>
<ul>
<li>객체 내부 데이터(필드)를 직접 건드리지 못하게 하고</li>
<li>공개된 메서드(인터페이스)를 통해서만 상태를 변경하도록 설계</li>
<li>결과적으로 “아무 데서나 값 바꾸는 코드”를 줄여 <strong>안정적인 변경</strong>이 가능</li>
</ul>
<hr />
<h4 id="2-abstraction-추상화">2) Abstraction (추상화)</h4>
<blockquote>
<p><strong>불필요한 디테일은 감추고 핵심 기능만 드러내는 것</strong>
공통 특징을 뽑아 <strong>인터페이스/추상 클래스</strong>로 정의하고, 구체 구현은 구현체가 담당</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">핵심 포인트</span></p>
<ul>
<li>“무엇을 할 수 있는가(행동)”에 집중</li>
<li>“어떻게 하는가(구현)”는 뒤로 미룸</li>
<li>변경에 유연한 구조(확장/교체)가 쉬워짐</li>
</ul>
<hr />
<h4 id="3-polymorphism-다형성">3) Polymorphism (다형성)</h4>
<blockquote>
<p><strong>하나의 인터페이스가 여러 형태로 동작할 수 있는 성질</strong>
같은 메시지(메서드 호출)라도 객체에 따라 다른 동작이 가능</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">핵심 포인트</span></p>
<ul>
<li>호출하는 쪽은 “인터페이스에 메시지”만 보내고</li>
<li>실제 동작은 “구현체가 알아서” 수행 → 결합도 ↓</li>
</ul>
<hr />
<h4 id="4-inheritance-상속">4) Inheritance (상속)</h4>
<blockquote>
<p><strong>상위 클래스의 특성을 하위 클래스가 물려받아 확장하는 것</strong>
재사용성을 높이고 중복을 줄이지만, 과도한 상속은 결합도를 키울 수 있음</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">핵심 포인트</span></p>
<ul>
<li>기존 기능을 수정하지 않고 새로운 기능 추가 → 확장성</li>
<li>중복 제거 → 재사용성</li>
<li>단, 상속은 “is-a” 관계가 명확할 때만 사용하는 게 안전</li>
</ul>
<hr />
<h4 id="추상화-추상-클래스-vs-인터페이스">추상화: 추상 클래스 vs 인터페이스</h4>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>둘 다 “추상화” 도구지만 목적이 다르다.</strong></span></p>
</blockquote>
<p><span style="background-color: #f6f8fa;">차이 정리</span></p>
<ul>
<li><p><strong>추상 클래스(Abstract Class)</strong></p>
<ul>
<li>공통 기능을 <strong>재사용</strong>하려는 목적</li>
<li>일반 메서드 + 추상 메서드 모두 가능</li>
<li>인스턴스 변수(상태) 가질 수 있음</li>
</ul>
</li>
<li><p><strong>인터페이스(Interface)</strong></p>
<ul>
<li>구현을 <strong>강제(규약)</strong> 하려는 목적</li>
<li>“무엇을 제공해야 하는지”를 명확히 함</li>
<li>구현체 교체/확장이 쉬움</li>
</ul>
</li>
</ul>
<hr />
<h4 id="다형성-오버로딩-vs-오버라이딩">다형성: 오버로딩 vs 오버라이딩</h4>
<blockquote>
<p><span style="background-color: #fff5b1;"><strong>같은 이름을 쓰지만 ‘언제/왜’가 다르다.</strong></span></p>
</blockquote>
<p><span style="background-color: #f6f8fa;">차이 정리</span></p>
<ul>
<li><p><strong>오버로딩(Overloading)</strong> : 같은 이름의 메서드를 <strong>여러 개 정의</strong></p>
<ul>
<li>매개변수 <strong>개수/타입/순서</strong>가 달라야 함</li>
</ul>
</li>
<li><p><strong>오버라이딩(Overriding)</strong> : 상위 클래스 메서드를 하위 클래스에서 <strong>재정의</strong></p>
<ul>
<li>메서드 시그니처(이름/매개변수 타입·개수·순서) 동일</li>
<li>반환 타입 동일(또는 규칙 내 호환)</li>
<li>접근 제어자는 <strong>같거나 더 넓게</strong>만 변경 가능</li>
</ul>
</li>
</ul>
<blockquote>
<p>즉, <strong>오버로딩 = 같은 기능을 다양한 입력으로</strong>
<strong>오버라이딩 = 상속받은 기능을 객체 특성에 맞게 변경</strong></p>
</blockquote>
<hr />
<h4 id="tda-원칙-tell-dont-ask">TDA 원칙 (Tell, Don’t Ask)</h4>
<blockquote>
<p>📌 <span style="background-color: #d1ebf9;"><strong>핵심</strong></span>
객체의 데이터를 꺼내서 판단/수정하지 말고, <strong>객체에게 “해줘”라고 메시지를 보내라.</strong>
→ 캡슐화 유지, 응집도 ↑, 결합도 ↓</p>
</blockquote>
<p><span style="background-color: #f6f8fa;">위반 예시 (Bad)</span></p>
<pre><code class="language-java">public class Account {

    private BigDecimal balance;

    public Account(BigDecimal balance) {
        this.balance = balance;
    }

    public BigDecimal getBalance() {
        return this.balance;
    }

    public void setBalance(BigDecimal balance) {
        this.balance = balance;
    }
}

Account account = new Account(BigDecimal.TEN);
BigDecimal withdrawalAmount = BigDecimal.ONE;

BigDecimal balance = account.getBalance(); // 데이터를 직접 가져와서 판단
if (balance.compareTo(withdrawalAmount) &lt; 0) {
    throw new IllegalStateException(&quot;잔액이 부족합니다.&quot;);
}

balance = balance.subtract(withdrawalAmount);
account.setBalance(balance); // 외부에서 상태를 직접 변경</code></pre>
<p><span style="background-color: #f6f8fa;">준수 예시 (Good)</span></p>
<pre><code class="language-java">public class Account {

    private BigDecimal balance;

    public Account(BigDecimal balance) {
        this.balance = balance;
    }

    public void withdraw(BigDecimal withdrawalAmount) {
        if (balance.compareTo(withdrawalAmount) &lt; 0) {
            throw new IllegalStateException(&quot;잔액이 부족합니다.&quot;);
        }
        this.balance = balance.subtract(withdrawalAmount);
    }
}

Account account = new Account(BigDecimal.TEN);
BigDecimal withdrawalAmount = BigDecimal.ONE;

account.withdraw(withdrawalAmount); // 객체에 메시지 전달</code></pre>
<hr />
<h4 id="한눈에-정리">한눈에 정리</h4>
<ul>
<li>OOP는 <strong>객체(상태+행위)</strong> 를 중심으로 역할/책임을 나눠 <strong>협력</strong>한다.</li>
<li>핵심 4가지: <span style="background-color: #fff5b1;">캡슐화/추상화/다형성/상속</span></li>
<li>추상화 도구: <strong>추상 클래스(재사용)</strong> vs <strong>인터페이스(규약/강제)</strong></li>
<li>다형성 구현: <strong>오버로딩(입력 다양화)</strong> vs <strong>오버라이딩(행동 재정의)</strong></li>
<li>TDA: “데이터 꺼내지 말고, 객체에게 시켜라” → <strong>캡슐화 지키는 실전 원칙</strong></li>
</ul>