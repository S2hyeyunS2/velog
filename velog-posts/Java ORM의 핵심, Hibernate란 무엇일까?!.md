<p><span style="background-color: #fff5b1;"><strong>Hibernate (하이버네이트)</strong></span>는 자바에서 가장 널리 사용되는 <strong>ORM (Object-Relational Mapping)</strong> 프레임워크 중 하나</p>
<hr />
<h3 id="🔍-hibernate란">🔍 <strong>Hibernate란?</strong></h3>
<ul>
<li>Hibernate는 자바 객체를 데이터베이스의 테이블과 매핑하여, 객체 지향적인 방식으로 데이터베이스와 상호 작용할 수 있게 해주는 <span style="background-color: #fff5b1;"> <strong>ORM 프레임워크</strong></span></li>
<li>복잡한 SQL을 직접 작성하지 않고도 자바 객체를 데이터베이스의 레코드로 저장하고 조회하는 것을 가능</li>
</ul>
<hr />
<h3 id="📝-주요-특징">📝 <strong>주요 특징</strong></h3>
<ol>
<li><p><strong>ORM (Object-Relational Mapping)</strong></p>
<ul>
<li>자바 객체와 데이터베이스 테이블의 <strong>1:1 매핑</strong>을 지원</li>
<li>객체의 필드를 테이블의 컬럼에, 객체의 인스턴스를 테이블의 행에 대응</li>
</ul>
</li>
<li><p><strong>HQL (Hibernate Query Language)</strong></p>
<ul>
<li>SQL과 유사하지만 객체 지향적 구조를 갖춘 쿼리 언어</li>
<li>데이터베이스 독립적인 쿼리를 작성할 수 있다</li>
</ul>
</li>
<li><p><strong>자동 관리 기능</strong></p>
<ul>
<li><strong>캐시</strong>를 이용한 성능 최적화</li>
<li><strong>트랜잭션 관리</strong> (ACID 보장)</li>
<li><strong>지연 로딩 (Lazy Loading)</strong>, <strong>즉시 로딩 (Eager Loading)</strong> 지원</li>
<li><strong>자동 스키마 생성</strong> (DDL 자동 생성)</li>
</ul>
</li>
<li><p><strong>JPA (Java Persistence API) 표준 구현체</strong></p>
<ul>
<li>JPA는 자바의 표준 퍼시스턴스 (영속성) API</li>
<li>Hibernate는 JPA의 기본 사양을 구현한 가장 대표적인 구현체</li>
</ul>
</li>
</ol>
<hr />
<h3 id="🗂️-hibernate의-주요-컴포넌트">🗂️ <strong>Hibernate의 주요 컴포넌트</strong></h3>
<ul>
<li><strong>SessionFactory</strong>: 데이터베이스 연결을 관리하고 세션을 생성</li>
<li><strong>Session</strong>: 데이터베이스 작업을 수행하는 단위</li>
<li><strong>Transaction</strong>: 작업의 논리적 단위로 -&gt; 성공하면 커밋, 실패하면 롤백</li>
<li><strong>Configuration</strong>: 설정 파일을 읽고 SessionFactory를 생성하는 데 사용</li>
<li><strong>Query</strong>: 데이터베이스에서 데이터를 조회하기 위한 객체</li>
</ul>
<hr />
<h3 id="⚙️-hibernate를-사용하는-이유">⚙️ <strong>Hibernate를 사용하는 이유</strong></h3>
<ul>
<li><strong>생산성</strong>: SQL을 직접 작성하지 않아도 되므로 개발 속도 향상</li>
<li><strong>유지보수성</strong>: 객체와 데이터베이스의 매핑 구조가 명확하여 코드의 가독성 증가</li>
<li><strong>데이터베이스 독립성</strong>: 다양한 데이터베이스와 쉽게 통합 가능</li>
<li><strong>성능 최적화</strong>: 캐시와 지연 로딩을 통한 성능 향상</li>
</ul>
<hr />
<h3 id="🛠️-간단한-hibernate-설정-예시">🛠️ <strong>간단한 Hibernate 설정 (예시)</strong></h3>
<pre><code class="language-java">// Employee.java (Entity 클래스)
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Table;
import jakarta.persistence.Column;

@Entity
@Table(name = &quot;employees&quot;)
public class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String department;

    // 기본 생성자
    public Employee() {
    }

    // 필드를 초기화하는 생성자
    public Employee(String name, String department) {
        this.name = name;
        this.department = department;
    }

    // Getter와 Setter
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    @Override
    public String toString() {
        return &quot;Employee{&quot; +
                &quot;id=&quot; + id +
                &quot;, name='&quot; + name + '\'' +
                &quot;, department='&quot; + department + '\'' +
                '}';
    }
}
</code></pre>
<pre><code class="language-xml">&lt;!-- hibernate.cfg.xml --&gt;
&lt;hibernate-configuration&gt;
    &lt;session-factory&gt;
        &lt;property name=&quot;hibernate.connection.driver_class&quot;&gt;com.mysql.cj.jdbc.Driver&lt;/property&gt;
        &lt;property name=&quot;hibernate.connection.url&quot;&gt;jdbc:mysql://localhost:3306/mydb&lt;/property&gt;
        &lt;property name=&quot;hibernate.connection.username&quot;&gt;root&lt;/property&gt;
        &lt;property name=&quot;hibernate.connection.password&quot;&gt;password&lt;/property&gt;
        &lt;property name=&quot;hibernate.dialect&quot;&gt;org.hibernate.dialect.MySQLDialect&lt;/property&gt;
        &lt;property name=&quot;hibernate.hbm2ddl.auto&quot;&gt;update&lt;/property&gt;
    &lt;/session-factory&gt;
&lt;/hibernate-configuration&gt;</code></pre>
<hr />
<h3 id="🌱-spring-data-jpa와의-관계">🌱 <strong>Spring Data JPA와의 관계</strong></h3>
<ul>
<li>Spring Data JPA는 JPA의 기능을 더 쉽게 사용할 수 있도록 Spring에서 제공하는 모듈</li>
<li>Hibernate는 JPA의 구현체이므로, Spring Data JPA는 기본적으로 Hibernate 위에서 동작하는 경우가 많다</li>
</ul>