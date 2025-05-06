<h1 id="spring-boot-3x-resttemplate--apache-httpclient-설정-시-주의할-점-httpclient5-대응">[Spring Boot 3.x] RestTemplate + Apache HttpClient 설정 시 주의할 점 (HttpClient5 대응)</h1>
<p>최근 Spring Boot 3.x + Java 21 환경으로 프로젝트를 시작하면서 <code>RestTemplate</code>을 커스터마이징하던 중, <strong>Apache HttpClient 관련 예제 대부분이 작동하지 않는 문제</strong>를 겪었습니다.</p>
<p>Spring Boot 3.x부터는 내부 의존성과 라이브러리 구조가 크게 바뀌었고,
특히 <code>Apache HttpClient</code> 관련 코드에서 문제를 경험하는 분들도 계실 거라 생각되어 정리해봅니다. 😊</p>
<hr />
<h2 id="❓-문제-상황">❓ 문제 상황</h2>
<p>Spring Boot 3.x에서 외부 API 호출을 위해 RestTemplate을 다음과 같이 설정했습니다.</p>
<pre><code class="language-java">@Bean
public RestTemplate restTemplate() {
    var factory = new HttpComponentsClientHttpRequestFactory();
    factory.setReadTimeout(1500);
    factory.setConnectTimeout(3000);
    factory.setHttpClient(HttpClientBuilder.create().build());
    return new RestTemplate(factory);
}</code></pre>
<p>하지만 이 코드는 <strong>Spring Boot 3.x에서는 컴파일 또는 런타임 에러가 발생</strong>합니다.</p>
<h3 id="📌-주의할-점">📌 주의할 점</h3>
<ul>
<li><code>setReadTimeout</code>, <code>setConnectTimeout</code> 등 일부 메서드가 동작하지 않거나 누락됩니다.</li>
<li>내부적으로 사용된 <code>org.apache.httpcomponents:httpclient</code>가 더 이상 기본 지원되지 않습니다.</li>
</ul>
<hr />
<h2 id="📎-원인-분석">📎 원인 분석</h2>
<p>Spring Boot 3.x는 Spring Framework 6.0을 기반으로 하며,
기존의 <code>Apache HttpClient 4.x</code> 라이브러리 대신 <strong>HttpClient 5.x</strong>를 사용합니다.</p>
<h3 id="✨-핵심-변경점">✨ 핵심 변경점</h3>
<ul>
<li><code>HttpClient 4.x</code>: <code>org.apache.httpcomponents:httpclient</code></li>
<li><code>HttpClient 5.x</code>: <code>org.apache.hc.client5:httpclient5</code></li>
</ul>
<p>이 두 버전은 API 구조가 상당히 다릅니다.
예제에서 쓰이던 <code>RequestConfig</code>, <code>setSocketTimeout</code>, <code>HttpClientBuilder</code> 등의 사용 방식이 완전히 달라졌습니다.</p>
<blockquote>
<p>공식 마이그레이션 가이드 보기 👉
<a href="https://hc.apache.org/httpcomponents-client-5.3.x/migration-guide/preparation.html">Apache HttpClient 4.x → 5.x Migration</a></p>
</blockquote>
<hr />
<h2 id="⚒-해결-방법-httpclient-5x-기준으로-작성">⚒ 해결 방법: HttpClient 5.x 기준으로 작성</h2>
<p>HttpClient 5.x에서는 <code>ConnectionManager</code>를 통한 설정이 기본이며,
<code>setReadTimeout</code> 같은 간단한 방식이 사라졌습니다.</p>
<h3 id="✅-httpclient-5x--resttemplate-구성-예시">✅ HttpClient 5.x + RestTemplate 구성 예시</h3>
<pre><code class="language-java">static final int READ_TIMEOUT = 1500;
static final int CONN_TIMEOUT = 3000;

@Bean
public RestTemplate restTemplate() {
    var factory = new HttpComponentsClientHttpRequestFactory();
    factory.setHttpClient(createHttpClient());
    return new RestTemplate(factory);
}

private HttpClient createHttpClient() {
    return HttpClientBuilder.create()
            .setConnectionManager(createHttpClientConnectionManager())
            .build();
}

private HttpClientConnectionManager createHttpClientConnectionManager() {
    return PoolingHttpClientConnectionManagerBuilder.create()
            .setDefaultConnectionConfig(
                ConnectionConfig.custom()
                    .setSocketTimeout(READ_TIMEOUT, TimeUnit.MILLISECONDS)
                    .setConnectTimeout(CONN_TIMEOUT, TimeUnit.MILLISECONDS)
                    .build()
            )
            .build();
}</code></pre>
<h3 id="설정-포인트">설정 포인트</h3>
<ul>
<li><code>ConnectionConfig</code>: timeout 관련 설정을 관리합니다.</li>
<li><code>PoolingHttpClientConnectionManagerBuilder</code>: 커넥션 풀 + 설정을 위한 빌더입니다.</li>
<li><code>HttpClientBuilder</code>: 최종적으로 HttpClient 인스턴스를 생성합니다.</li>
</ul>
<hr />
<h2 id="📌-비교-요약">📌 비교 요약</h2>
<table>
<thead>
<tr>
<th>항목</th>
<th>HttpClient 4.x (지원 X)</th>
<th>HttpClient 5.x (권장)</th>
</tr>
</thead>
<tbody><tr>
<td>라이브러리</td>
<td><code>org.apache.httpcomponents:httpclient</code></td>
<td><code>org.apache.hc.client5:httpclient5</code></td>
</tr>
<tr>
<td>설정 방식</td>
<td><code>setReadTimeout()</code> 등 직접 설정</td>
<td><code>ConnectionConfig</code> + <code>ConnectionManager</code></td>
</tr>
<tr>
<td>RestTemplate factory</td>
<td>여전히 <code>HttpComponentsClientHttpRequestFactory</code> 사용 가능</td>
<td>가능, 단 내부 HttpClient는 5.x 구조로 설정해야 함</td>
</tr>
</tbody></table>
<hr />
<h2 id="📦-gradle-buildgradle-의존성-추가">📦 Gradle (build.gradle) 의존성 추가</h2>
<pre><code class="language-groovy">dependencies {
    implementation 'org.apache.httpcomponents.client5:httpclient5:5.3'
}</code></pre>
<hr />
<h2 id="🔗-참고-문서">🔗 참고 문서</h2>
<ul>
<li><a href="https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide#apache-httpclient-in-resttemplate">Spring Boot 3.0 Migration Guide – Apache HttpClient</a></li>
<li><a href="https://hc.apache.org/httpcomponents-client-5.3.x/migration-guide/preparation.html">Apache HttpClient 5.x Migration Guide</a></li>
</ul>