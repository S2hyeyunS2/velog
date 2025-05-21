<p>알고리즘 문제에서 <strong>공백이나 특정 구분자로 구분된 데이터를 빠르게 파싱</strong>해야 할 때 <strong>StringTokenizer</strong>는 매우 유용하다</p>
<hr />
<h2 id="📌-stringtokenizer란">📌 StringTokenizer란?</h2>
<p><strong>StringTokenizer</strong>는 문자열을 특정 구분자를 기준으로 나누어 <strong>토큰(Token)</strong> 단위로 분리하는 데 사용한다. 
자바의 <strong>레거시 클래스</strong> 중 하나로, 주로 알고리즘 문제나 대용량 데이터의 파싱에서 사용된다.</p>
<h3 id="🛠-주요-특징"><strong>🛠 주요 특징</strong></h3>
<ul>
<li><strong>구분자 기반</strong>: 기본적으로 공백을 구분자로 사용하지만, 사용자가 원하는 구분자를 지정할 수도 있다.</li>
<li><strong>비동기성</strong>: 스레드 세이프하지 않지만 매우 빠르다.</li>
<li><strong>토큰 단위 접근</strong>: 분리된 토큰을 하나씩 순차적으로 접근할 수 있다.</li>
</ul>
<h3 id="📝-기본-사용법"><strong>📝 기본 사용법</strong></h3>
<pre><code class="language-java">import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        String input = &quot;Hello World Java Programming&quot;;

        // 기본 공백 분리
        StringTokenizer st = new StringTokenizer(input);

        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
    }
}</code></pre>
<p><strong>출력:</strong></p>
<pre><code>Hello
World
Java
Programming</code></pre><hr />
<h2 id="⚙️-구분자-지정하기">⚙️ 구분자 지정하기</h2>
<p>StringTokenizer는 기본적으로 공백을 구분자로 사용하지만, 구분자를 명시적으로 지정할 수도 있다.</p>
<pre><code class="language-java">import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        String data = &quot;2023-05-19,Java,Programming&quot;;

        // 콤마(,)를 구분자로 지정
        StringTokenizer st = new StringTokenizer(data, &quot;,&quot;);

        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
    }
}</code></pre>
<p><strong>출력:</strong></p>
<pre><code>2023-05-19
Java
Programming</code></pre><h3 id="🛠-여러-구분자-사용하기"><strong>🛠 여러 구분자 사용하기</strong></h3>
<pre><code class="language-java">import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        String data = &quot;Java|Python;C++/JavaScript,Go&quot;;

        // 여러 구분자 지정
        StringTokenizer st = new StringTokenizer(data, &quot;|;/,&quot;);

        while (st.hasMoreTokens()) {
            System.out.println(st.nextToken());
        }
    }
}</code></pre>
<p><strong>출력:</strong></p>
<pre><code>Java
Python
C++
JavaScript
Go</code></pre><hr />
<h2 id="📝-주요-메소드">📝 주요 메소드</h2>
<table>
<thead>
<tr>
<th>메소드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>hasMoreTokens()</code></td>
<td>다음 토큰이 있는지 확인 (boolean)</td>
</tr>
<tr>
<td><code>nextToken()</code></td>
<td>다음 토큰 반환 (String)</td>
</tr>
<tr>
<td><code>countTokens()</code></td>
<td>남은 토큰의 개수 반환 (int)</td>
</tr>
</tbody></table>
<hr />
<h2 id="💡-split-vs-stringtokenizer-비교">💡 split() vs StringTokenizer 비교</h2>
<table>
<thead>
<tr>
<th>특징</th>
<th><code>StringTokenizer</code></th>
<th><code>String.split()</code></th>
</tr>
</thead>
<tbody><tr>
<td><strong>속도</strong></td>
<td>빠름</td>
<td>비교적 느림 (정규식 파싱)</td>
</tr>
<tr>
<td><strong>구분자 지정</strong></td>
<td>단일 문자열 가능</td>
<td>정규 표현식 지원</td>
</tr>
<tr>
<td><strong>비어있는 토큰 처리</strong></td>
<td>무시</td>
<td>포함 (빈 문자열)</td>
</tr>
<tr>
<td><strong>출력 형식</strong></td>
<td>순차 접근</td>
<td>배열 반환</td>
</tr>
</tbody></table>
<hr />
<h2 id="🚀-백준-15552번">🚀 백준 15552번</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i &lt; T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            System.out.println(A + B);
        }

        br.close();
    }
}</code></pre>
<ul>
<li><strong>빠른 입력</strong>: <code>BufferedReader</code></li>
<li><strong>효율적 파싱</strong>: <code>StringTokenizer</code></li>
</ul>
<hr />
<h2 id="🚫-단점">🚫 단점</h2>
<ul>
<li><strong>레거시 클래스</strong>: JDK 1.0에서 도입된 오래된 클래스</li>
<li><strong>정규 표현식 미지원</strong>: 단순한 구분자만 처리 가능</li>
<li><strong>비어있는 토큰 무시</strong>: 공백이 있는 경우 누락될 수 있음</li>
</ul>