<h3 id="📌-restful-api란">📌 RESTful API란?</h3>
<ul>
<li>RESTful API는 <strong>REST(Representational State Transfer) 원칙을 따르는 API를 의미</strong></li>
<li>클라이언트(웹, 앱 등)와 서버가 HTTP를 통해 데이터를 주고받을 때, REST 원칙을 잘 따르는 API를 RESTful API라고 한다</li>
</ul>
<hr />
<h3 id="📌-rest의-주요-원칙">📌 REST의 주요 원칙</h3>
<h4 id="✅-1-자원resource-기반의-uri-설계">✅** 1. 자원(Resource) 기반의 URI 설계**</h4>
<ul>
<li>RESTful API에서는 <strong>모든 데이터(자원)</strong>를 <strong>URI(Uniform Resource Identifier)</strong>로 표현</li>
</ul>
<pre><code class="language-bash">GET /api/calendars/{calendarId}/schedules  (일정 목록 조회)
POST /api/calendars/{calendarId}/schedules  (일정 생성)
GET /api/calendars/{calendarId}/schedules/{scheduleId}  (특정 일정 조회)
PUT /api/calendars/{calendarId}/schedules/{scheduleId}  (특정 일정 수정)
DELETE /api/calendars/{calendarId}/schedules/{scheduleId}  (특정 일정 삭제)</code></pre>
<p>URI 자체가 어떤 리소스를 조작하는지 명확하게 표현이 가능
GET, POST, PUT, DELETE 같은 HTTP 메서드를 활용해 동작을 표현</p>
<h4 id="✅-2-http-메서드-활용">✅ 2. HTTP 메서드 활용</h4>
<ul>
<li>RESTful API에서는 <strong>HTTP 메서드를 이용해 동작을 구분</strong></li>
<li><ul>
<li>GET : 조회</li>
</ul>
</li>
<li><ul>
<li>POST : 생성</li>
</ul>
</li>
<li><ul>
<li>PUT : 수정</li>
</ul>
</li>
<li><ul>
<li>DELETE : 삭제</li>
</ul>
</li>
</ul>
<pre><code class="language-http">GET /api/calendars/{calendarId}/schedules  # 일정 목록 조회
POST /api/calendars/{calendarId}/schedules  # 일정 생성
PUT /api/calendars/{calendarId}/schedules/{scheduleId}  # 일정 수정
DELETE /api/calendars/{calendarId}/schedules/{scheduleId}  # 일정 삭제</code></pre>
<h4 id="✅-3-무상태성-stateless">✅ 3. 무상태성 (Stateless)</h4>
<ul>
<li>각 <strong>요청(request)이 독립적으로 처리</strong></li>
<li>서버는 이전 요청 상태를 저장하지 않고 클라이언트가 매번 필요한 데이터를 전부 보내야 함</li>
</ul>
<pre><code class="language-http"># 요청 1: 사용자 로그인 (JWT 토큰 발급)
POST /api/auth/login
{
    &quot;username&quot;: &quot;chu42&quot;,
    &quot;password&quot;: &quot;1234&quot;
}
# 응답 (서버는 상태를 기억하지 않음. 클라이언트가 토큰을 저장해야 함)
{
    &quot;token&quot;: &quot;eyJhbGciOiJIUzI1...&quot;
}

# 요청 2: 일정 목록 조회 (클라이언트가 토큰을 보내야 함)
GET /api/calendars/{calendarId}/schedules
Authorization: Bearer eyJhbGciOiJIUzI1...</code></pre>
<p>서버가 불필요한 정보를 저장하지 않으므로, 확장성이 좋다</p>
<h4 id="✅-4-일관된-응답-형식-json">✅ 4. 일관된 응답 형식 (JSON)</h4>
<ul>
<li>RESTful API는 주로 JSON을 사용해서 데이터를 주고받음</li>
</ul>
<pre><code class="language-json">{
    &quot;id&quot;: 1,
    &quot;title&quot;: &quot;회의 일정&quot;,
    &quot;description&quot;: &quot;팀 회의&quot;,
    &quot;startTime&quot;: &quot;2025-02-26T10:00:00&quot;,
    &quot;endTime&quot;: &quot;2025-02-26T11:00:00&quot;,
    &quot;location&quot;: {
        &quot;latitude&quot;: 37.5665,
        &quot;longitude&quot;: 126.9780,
        &quot;address&quot;: &quot;서울특별시 중구 세종대로 110&quot;
    }
}</code></pre>
<p>JSON은 가볍고 모든 언어에서 쉽게 파싱이 가능
사람이 읽고 이해하기 쉬움</p>
<hr />
<h3 id="📌-정리-restful-api란">📌 정리 (RESTful API란?)</h3>
<p>✅ RESTful API란, REST 원칙을 따르는 API
✅ 자원을 URI로 표현하고 <strong>HTTP 메서드(GET, POST, PUT, DELETE)</strong>를 활용
✅ 서버는 상태를 저장하지 않음 (Stateless)
✅ 응답은 JSON 형식으로 일관성 유지</p>