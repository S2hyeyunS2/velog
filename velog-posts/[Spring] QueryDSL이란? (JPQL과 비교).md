<p>Querydsl은 Java 기반의 타입 안전한 쿼리(Query) 빌더 라이브러리
PA, SQL, MongoDB 등 여러 데이터 소스에 대해 컴파일 시점에 쿼리 오류를 방지할 수 있도록 도와줌</p>
<hr />
<h3 id="📌-querydsl의-주요-특징">📌 Querydsl의 주요 특징</h3>
<ul>
<li><p>타입 안전성 (Type-safe)
쿼리를 문자열(String)로 작성하는 대신, Java 코드로 작성해서 컴파일 시점에 오류를 잡을 수 있다</p>
</li>
<li><p>IDE 자동완성 지원
JPA 엔티티를 기반으로 Q타입 클래스를 생성하기 때문에, IDE에서 필드 자동완성 사용 가능</p>
</li>
<li><p>JPQL 대체
JPQL의 복잡한 문자열 문법을 피하고, 가독성 높고 유지보수가 쉬운 쿼리를 작성할 수 있다</p>
</li>
</ul>
<hr />
<h3 id="🔨-사용-예시">🔨 사용 예시</h3>
<p><strong>1. JPA 엔티티</strong></p>
<pre><code class="language-java">@Entity
public class Member {
    @Id @GeneratedValue
    private Long id;

    private String username;

    private int age;

    @ManyToOne
    private Team team;
}</code></pre>
<p><strong>2. Q타입 생성</strong></p>
<pre><code class="language-java">// build.gradle
annotationProcessor &quot;com.querydsl:querydsl-apt:5.0.0:jpa&quot;
implementation &quot;com.querydsl:querydsl-jpa:5.0.0&quot;</code></pre>
<p>Q타입은 QMember라는 이름으로 생성됨. 필드들은 다 static으로 되어 있어서 바로 접근이 가능</p>
<p><strong>3. Querydsl 쿼리 예시</strong></p>
<pre><code class="language-java">JPAQueryFactory queryFactory = new JPAQueryFactory(entityManager);
QMember m = QMember.member;

Member result = queryFactory
    .selectFrom(m)
    .where(m.username.eq(&quot;choi&quot;))
    .fetchOne();</code></pre>
<p>SQL로 바꾼다면</p>
<pre><code class="language-SQL">SELECT * FROM member WHERE username = 'choi';</code></pre>
<hr />
<h3 id="💡-동적-쿼리-예시">💡 동적 쿼리 예시</h3>
<pre><code class="language-java">public List&lt;Member&gt; search(String usernameCond, Integer ageCond) {
    return queryFactory
        .selectFrom(m)
        .where(
            usernameEq(usernameCond),
            ageEq(ageCond)
        )
        .fetch();
}

private BooleanExpression usernameEq(String username) {
    return username != null ? m.username.eq(username) : null;
}

private BooleanExpression ageEq(Integer age) {
    return age != null ? m.age.eq(age) : null;
}</code></pre>
<hr />
<h3 id="🆚-jpql-vs-querydsl">🆚 JPQL vs QueryDSL</h3>
<table>
<thead>
<tr>
<th>구분</th>
<th>JPQL</th>
<th>QueryDSL</th>
</tr>
</thead>
<tbody><tr>
<td><strong>작성 방식</strong></td>
<td>문자열(String) 기반</td>
<td>Java 코드 기반 (타입 안전)</td>
</tr>
<tr>
<td><strong>컴파일 타임 오류 검출</strong></td>
<td>❌ (런타임 오류)</td>
<td>✅ (컴파일 타임에 오류 검출)</td>
</tr>
<tr>
<td><strong>자동 완성 지원</strong></td>
<td>❌ (IDE에서 거의 불가능)</td>
<td>✅ (IDE 자동완성, 리팩토링 용이)</td>
</tr>
<tr>
<td><strong>가독성</strong></td>
<td>중간 (쿼리 짧을 땐 괜찮음)</td>
<td>높음 (복잡할수록 장점 극대화)</td>
</tr>
<tr>
<td><strong>동적 쿼리</strong></td>
<td>복잡하고 번거로움</td>
<td>간단하고 깔끔함</td>
</tr>
<tr>
<td><strong>서브 쿼리/조인 등 고급 기능</strong></td>
<td>지원됨 (문자열로 처리)</td>
<td>동일하게 지원되며, 더 깔끔하게 처리</td>
</tr>
<tr>
<td><strong>학습 난이도</strong></td>
<td>낮음 (SQL 비슷)</td>
<td>중간 (초반엔 낯설 수 있음)</td>
</tr>
</tbody></table>
<hr />
<h2 id="🔍-예시-비교">🔍 예시 비교</h2>
<h3 id="📝-jpql">📝 JPQL</h3>
<pre><code class="language-java">String jpql = &quot;SELECT m FROM Member m WHERE m.username = :username&quot;;
Member member = em.createQuery(jpql, Member.class)
                  .setParameter(&quot;username&quot;, &quot;choi&quot;)
                  .getSingleResult();</code></pre>
<ul>
<li>문자열이라 오타 나면 런타임에서만 오류가 나고 리팩토링이나 필드 변경에 약함</li>
</ul>
<hr />
<h3 id="⚙️-querydsl">⚙️ QueryDSL</h3>
<pre><code class="language-java">QMember m = QMember.member;

Member member = queryFactory
    .selectFrom(m)
    .where(m.username.eq(&quot;choi&quot;))
    .fetchOne();</code></pre>
<ul>
<li><code>username</code> 필드 이름 바뀌면 컴파일 에러 발생 (안전!)</li>
<li>IDE 자동완성 가능</li>
<li>동적 쿼리나 조건 조합이 훨씬 수월</li>
</ul>
<hr />
<h3 id="✅-결론">✅ 결론</h3>
<ul>
<li><strong>간단한 쿼리</strong>나 <strong>빠르게 써야 하는 경우</strong>엔 JPQL도 괜찮</li>
<li>하지만 <strong>복잡한 조건</strong>, <strong>동적 쿼리</strong>, <strong>유지보수</strong>, <strong>리팩토링</strong> 생각한다면 <strong>QueryDSL이 훨씬 유리</strong></li>
</ul>