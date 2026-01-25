<h3 id="java-객체-지향-설계의-5원칙-solid"> 객체 지향 설계의 5원칙, SOLID</h3>
<blockquote>
<p>📋 <span style="background-color: #fff5b1;"><strong>한 줄 요약</strong></span><br />SOLID는 객체지향 설계에서 <strong>유지보수성과 확장성</strong>을 높이기 위한 _<strong>5가지 설계 원칙</strong>_이다.<br />적용하면 코드 확장이 쉬워지고, 유지보수가 편해지며, 불필요한 복잡도를 줄여 리팩토링 비용을 낮출 수 있다.</p>
</blockquote>
<hr />
<p><span style="background-color: #f6f8fa;">구성</span></p>
<p>✔️ <strong>SRP</strong> (Single Responsibility Principle): 단일 책임 원칙<br />✔️ <strong>OCP</strong> (Open Closed Principle): 개방 폐쇄 원칙<br />✔️ <strong>LSP</strong> (Liskov Substitution Principle): 리스코프 치환 원칙<br />✔️ <strong>ISP</strong> (Interface Segregation Principle): 인터페이스 분리 원칙<br />✔️ <strong>DIP</strong> (Dependency Inversion Principle): 의존 역전 원칙  </p>
<hr />
<h3 id="1-srp-단일-책임-원칙-single-responsibility-principle">1) SRP 단일 책임 원칙 (Single Responsibility Principle)</h3>
<p><span style="background-color: #fff5b1;"><strong>클래스(객체)는 단 하나의 책임(기능)만 가져야 한다</strong></span></p>
<h3 id="핵심-개념">핵심 개념</h3>
<ul>
<li>하나의 클래스는 <strong>하나의 기능을 담당</strong>하고 그 책임에 집중해야 한다.  </li>
<li>하나의 클래스가 여러 기능을 가지면, 수정 시 영향을 받는 코드가 늘어나 <strong>변경 범위가 커진다.</strong>  </li>
<li>책임이 많아질수록 서로 다른 역할의 코드가 얽혀 <strong>결합도는 증가</strong>하고 시스템은 복잡해질 수 있다.  </li>
<li>변경 사항이 발생하면 관련 기능을 사용하는 부분까지 <strong>재테스트 범위가 커질 수 있다.</strong></li>
</ul>
<blockquote>
<p>SRP의 목적은 <span style="background-color: #fff5b1;"><strong>프로그램의 유지보수성을 높이는 것</strong></span>이다.<br />한 책임의 변경이 다른 책임 변경으로 이어지는 <strong>연쇄작용을 줄인다.</strong></p>
</blockquote>
<h3 id="예제-상황-및-코드">예제 상황 및 코드</h3>
<pre><code class="language-java">@Transactional
@Override
public CompanyResult createCompany(CreateCompanyCommand cmd, Long userId, String userRole) {
    companyValidator.assertCreateAccess(cmd.hubId(), userId, userRole);
    companyValidator.assertHubExists(cmd.hubId());
    companyValidator.assertCompanyNotDuplicated(cmd.hubId(), cmd.name());

    Company company =
            Company.create(cmd.hubId(), cmd.name(), cmd.type(), cmd.slackId(), cmd.address());
    Company saved = companyRepository.save(company);

    return CompanyResult.from(saved);
}</code></pre>
<p>만약 검증들이 전부 서비스에 섞여있으면, 권한 정책 변경이나, 중복 정책 변경 등이 모두 같은 클래스 변경으로 이어져서 SRP가 깨지기 쉽다.</p>
<h3 id="srp-적용-시-주의할-점">SRP 적용 시 주의할 점</h3>
<p><span style="background-color: #f6f8fa;"><strong>1) 클래스명은 책임의 소재가 드러나게</strong></span><br />클래스가 무엇을 담당하는지 이름만 봐도 알 수 있도록 작명한다.</p>
<p><span style="background-color: #f6f8fa;"><strong>2) 책임 분리 시 결합도/응집도 함께 고려</strong></span></p>
<ul>
<li>무작정 쪼개면 오히려 파편화되어 복잡도가 증가할 수 있다.</li>
<li>좋은 설계는 <strong>응집도는 높게</strong>, <strong>결합도는 낮게</strong> 유지한다.</li>
<li>책임 간 결합도를 최소화하되, 너무 쪼개져 응집력이 떨어지면 다시 묶는 설계가 필요하다.</li>
</ul>
<hr />
<h2 id="2-ocp-개방-폐쇄-원칙-open-closed-principle">2) OCP 개방 폐쇄 원칙 (Open Closed Principle)</h2>
<p> <span style="background-color: #fff5b1;"><strong>확장에는 열려 있고, 수정에는 닫혀 있어야 한다</strong></span></p>
<h3 id="핵심-개념-1">핵심 개념</h3>
<ul>
<li>기능 추가 요청이 들어오면 <strong>클래스 확장으로 손쉽게 구현</strong>하고<br />확장에 따른 <strong>기존 코드 수정은 최소화</strong>해야 한다.</li>
<li>즉, 기존 코드를 변경하지 않으면서 새로운 기능을 추가할 수 있도록 설계한다.</li>
</ul>
<p><span style="background-color: #f6f8fa;"><strong>[ 확장에 열려 있다 ]</strong></span><br />새로운 변경 사항이 발생했을 때 유연하게 코드를 추가하여 애플리케이션의 기능을 큰 힘 들이지 않고 확장할 수 있음을 의미한다.</p>
<p><span style="background-color: #f6f8fa;"><strong>[ 변경에 닫혀 있다 ]</strong></span><br />새로운 변경 사항이 발생했을 때 객체를 직접 수정하는 행위를 제한해야 함을 의미한다.<br />객체를 자주 직접 수정해야 한다면 유지보수 비용이 증가하고 변경에 유연하지 못한 구조가 된다.</p>
<blockquote>
<p>OCP는 <span style="background-color: #fff5b1;"><strong>추상화를 통한 관계 구축</strong></span>을 권장하며,<br />다형성과 확장을 가능하게 하는 객체지향의 장점을 극대화하는 원칙이다.</p>
</blockquote>
<h3 id="예제-상황-및-코드-1">예제 상황 및 코드</h3>
<pre><code class="language-Java">  public interface CompanyRepository {
    Company save(Company company);
    Optional&lt;Company&gt; findById(UUID companyId);
    boolean existsByHubIdAndName(UUID hubId, String companyName);
    Page&lt;Company&gt; search(SearchCompanyCommand cmd, Pageable pageable);
}</code></pre>
<p>검색 조건 (지역, 생성일, 삭제여부, 정렬 등)이 계속 늘어나면 구현체 쿼리/조건문이 커지면서 수정이 많아질 수 있다.
이럴 때 조건 객체/전략/스펙 등을 도입해 확장 중심으로 가져가면 좋다</p>
<h3 id="ocp-적용-시-주의할-점">OCP 적용 시 주의할 점</h3>
<ul>
<li><strong>추상화</strong>는 다양한 객체를 구분할 수 있게 하는 “본질적인 특징”을 정의하는 것이다.</li>
<li>추상 메서드를 설계할 때는 <strong>적당한 추상화 레벨</strong>을 선택해야 한다.</li>
<li>핵심 행위의 본질을 정의하고, 구체 행위는 서브 타입에 위임해 관계를 성립시키는 방식이 된다.</li>
</ul>
<hr />
<h2 id="3-lsp-리스코프-치환-원칙-liskov-substitution-principle">3) LSP 리스코프 치환 원칙 (Liskov Substitution Principle)</h2>
<p><span style="background-color: #fff5b1;"><strong>서브 타입은 언제나 부모 타입으로 교체할 수 있어야 한다</strong></span></p>
<h3 id="핵심-개념-2">핵심 개념</h3>
<ul>
<li>다형성을 위해 상위 타입으로 객체를 선언하고 하위 타입 인스턴스를 받더라도,<br /><strong>부모 타입의 메서드를 호출했을 때 동작이 의도대로 흘러가야 한다.</strong></li>
<li>자식 클래스가 부모 메서드를 오버라이딩할 때, 부모 클래스가 기대하는 선행 조건/행동 규약을 깨면<br />사용 코드에서 예상치 못한 문제가 발생할 수 있다.</li>
</ul>
<h3 id="예시">예시</h3>
<p>자바에서 <code>Collection</code> 인터페이스를 예로 들 수 있다.<br /><code>Collection</code> 타입에서 구현체를 <code>LinkedList</code>에서 <code>HashSet</code>으로 바꾸더라도 <code>add()</code> 같은 메서드는 의도대로 동작한다.<br />즉, 상위 타입으로 메서드를 실행해도 정상 동작하도록 구성되어야 한다.</p>
<h3 id="예제-상황-및-코드-2">예제 상황 및 코드</h3>
<pre><code class="language-Java">@RequiredArgsConstructor
public class CompanyServiceImpl implements CompanyService {

    private final CompanyRepository companyRepository;
    private final CompanyValidator companyValidator;

    // ...
}</code></pre>
<p>Company 서비스는 Repository를 인터페이스 타입으로 받고 있다
CompanyRepository 구현체가 어떤 형태로 바뀌더라도 CompanyServiceImpl은 같은 계약을 믿고 동작한다.</p>
<h3 id="lsp-적용-시-주의할-점">LSP 적용 시 주의할 점</h3>
<p><span style="background-color: #f6f8fa;"><strong>1) 부모 타입의 행동 규약을 위반하면 안 된다</strong></span><br />오버라이딩을 잘못 정의하면 LSP 위반이 된다.</p>
<p><span style="background-color: #f6f8fa;"><strong>2) 상속은 IS-A 관계에서만 제한적으로 사용</strong></span><br />기반 클래스와 서브 클래스 사이에 명확한 IS-A 관계가 성립할 때만 상속을 적용한다.</p>
<p><span style="background-color: #f6f8fa;"><strong>3) 상속 대신 더 나은 선택지 고려</strong></span></p>
<ul>
<li>다형성을 원하면 <code>extends</code>보다 <strong>인터페이스 <code>implements</code></strong>로 상위 타입을 맞추는 방식이 적합할 수 있다.</li>
<li>기능 재사용이 목적이라면 <strong>상속보다 합성(Composition)</strong>이 더 안전한 선택일 수 있다.</li>
</ul>
<hr />
<h2 id="4-isp-인터페이스-분리-원칙-interface-segregation-principle">4) ISP 인터페이스 분리 원칙 (Interface Segregation Principle)</h2>
<p><span style="background-color: #fff5b1;"><strong>인터페이스는 사용 목적에 맞게 잘게 분리해야 한다</strong></span></p>
<h3 id="핵심-개념-3">핵심 개념</h3>
<ul>
<li>인터페이스를 사용하는 <strong>클라이언트를 기준으로 분리</strong>해야 한다.</li>
<li>클라이언트의 목적/용도에 맞는 인터페이스만 제공함으로써 불필요한 의존을 줄인다.</li>
<li>인터페이스는 다중 구현이 가능하므로, 분리할 수 있다면 분리하여 각 클래스 용도에 맞게 <code>implements</code>하는 것이 바람직하다.</li>
</ul>
<h3 id="isp-예시">(ISP 예시)</h3>
<pre><code class="language-Java">@FeignClient(name = &quot;user-service&quot;)
public interface UserClient {

    @GetMapping(&quot;/v1/user/{id}&quot;)
    UserDTO getUser(
            @PathVariable(&quot;id&quot;) Long id,
            @RequestHeader(&quot;X-User-Id&quot;) Long requestUserId,
            @RequestHeader(&quot;X-User-Role&quot;) String requestUserRole);

    record UserDTO(
            Long userId,
            String username,
            String name,
            String slackId,
            String phoneNumber,
            String role,
            String status,
            UUID companyId) {}
}</code></pre>
<pre><code class="language-Java">@FeignClient(name = &quot;hub-service&quot;)
public interface HubClient {
    @GetMapping(&quot;/v1/hubs/{hubId}&quot;)
    HubDTO getHub(@PathVariable UUID hubId);

    record HubDTO(UUID hubId, String name, String address) {}
}</code></pre>
<p>Company는 허브/유저 정보를 가져오기 위해 FeignClient를 분리해 두었다.</p>
<h3 id="isp-적용-시-주의할-점">ISP 적용 시 주의할 점</h3>
<blockquote>
<p>이미 구현되어 있는 프로젝트에서 인터페이스를 또 쪼개면,<br />해당 인터페이스를 구현하고 있던 클래스들과 이를 사용하는 클라이언트 코드에서 변경 파급이 발생할 수 있다.</p>
</blockquote>
<hr />
<h2 id="5-dip-의존-역전-원칙-dependency-inversion-principle">5) DIP 의존 역전 원칙 (Dependency Inversion Principle)</h2>
<p><span style="background-color: #fff5b1;"><strong>구체 클래스가 아니라 상위 요소(추상화)에 의존하라</strong></span></p>
<h3 id="핵심-개념-4">핵심 개념</h3>
<ul>
<li>어떤 클래스를 참조해서 사용해야 한다면, 그 클래스를 직접 참조하는 것이 아니라<br /><strong>그 대상의 상위 요소(추상 클래스/인터페이스)</strong> 를 참조해야 한다.</li>
<li>의존 관계를 맺을 때는 변화하기 쉬운 것보다, <strong>변화하기 어려운 것(추상화)</strong> 에 의존해야 한다.</li>
<li>DIP의 지향점은 클래스 간 <strong>결합도(coupling)를 낮추는 것</strong>이다.</li>
</ul>
<p><span style="background-color: #f6f8fa;"><strong>클래스 간 의존 관계란?</strong></span><br />한 클래스가 기능을 수행하기 위해 다른 클래스의 서비스가 필요한 경우를 말한다.<br />예를 들어 A 클래스가 메서드 파라미터로 B 타입을 받아 B의 기능을 사용하는 경우, A는 B에 의존한다고 볼 수 있다.</p>
<blockquote>
<p>하위 모듈(구현체)의 구체 내용에 직접 의존하면,<br />하위 모듈 변화 때마다 클라이언트/상위 모듈을 자주 수정해야 한다.<br />따라서 구현이 아닌 <span style="background-color: #fff5b1;"><strong>추상화</strong></span>에 의존하도록 설계한다.</p>
</blockquote>
<h3 id="dip-예시">(DIP 예시)</h3>
<pre><code class="language-Java">public interface CompanyService {
    CompanyResult createCompany(CreateCompanyCommand cmd, Long userId, String userRole);
    CompanyResult updateCompany(UpdateCompanyCommand cmd, Long userId, String userRole);
    CompanyResult getCompany(UUID companyId);
    CommonPageResponse&lt;CompanyResult&gt; searchCompany(SearchCompanyCommand cmd, CommonPageRequest pageReq);
    CompanyResult changeStatus(ChangeCompanyStatusCommand cmd, Long userId, String userRole);
    void deleteCompany(UUID companyId, Long userId, String userRole);
}</code></pre>
<pre><code class="language-Java">@RequiredArgsConstructor
public class CompanyServiceImpl implements CompanyService {
    private final CompanyRepository companyRepository;
    private final CompanyValidator companyValidator;
}</code></pre>
<pre><code class="language-Java">@RestController
@RequiredArgsConstructor
public class CompanyController {
    private final CompanyService companyService;
}</code></pre>
<p>서비스는 저장소 구현(JPA 등)이 아니라 도메인 레벨 Repository 인터페이스에 의존
컨트롤러는 구현체가 아니라 Service 인터페이스에 의존
즉, 상위 계층(Controller, Service)은 하위 계층의 구체 클래스가 아니라 인터페이스를 바라본다.</p>