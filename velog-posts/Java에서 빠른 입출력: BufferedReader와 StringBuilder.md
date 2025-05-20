<p>나는 파이썬으로 코테를 준비하고 있다 
요즘 서류합격하고 코테보는 곳은 파이썬 지원을 안한다...!! 
그러다보니 급하게 JAVA도 공부하게 됐는데 코드길이가 2배이상이다
너무 슬프지만 어떻게 하겠음 ㅠㅡㅠ</p>
<p>Python에서는 입출력 속도 지원할 때 sys.stdin.readline()한줄이면 됐는데 자바는,, 길다 길어</p>
<hr />
<p>입출력 속도는 중요하다
Scanner는 간편하지만 느리기 때문에 BufferedReader와 StringBuilder를 사용하는게 훨씬 효율적이다</p>
<hr />
<h2 id="📌-scanner와-bufferedreader의-차이점">📌 Scanner와 BufferedReader의 차이점</h2>
<table>
<thead>
<tr>
<th>특징</th>
<th>Scanner</th>
<th>BufferedReader</th>
</tr>
</thead>
<tbody><tr>
<td>입력 방식</td>
<td>토큰 단위 입력 (공백 기준)</td>
<td>라인 단위 입력 (개행 기준)</td>
</tr>
<tr>
<td>속도</td>
<td>느림 (Parsing 포함)</td>
<td>매우 빠름 (직접 파싱 필요)</td>
</tr>
<tr>
<td>동기화</td>
<td>네</td>
<td>아니오</td>
</tr>
<tr>
<td>예외 처리</td>
<td>불필요</td>
<td>필수 (IOException)</td>
</tr>
<tr>
<td>편의성</td>
<td>높음</td>
<td>낮음 (StringTokenizer 필요)</td>
</tr>
<tr>
<td>주 사용 사례</td>
<td>일반적인 콘솔 입력</td>
<td>대량 데이터, 알고리즘 문제 풀이</td>
</tr>
</tbody></table>
<h3 id="🔍-왜-bufferedreader가-더-빠를까">🔍 왜 BufferedReader가 더 빠를까?</h3>
<ol>
<li><p><strong>버퍼링 처리</strong>:</p>
<ul>
<li><code>BufferedReader</code>는 내부적으로 <strong>8192바이트</strong>의 기본 버퍼를 사용하여 입력 속도를 크게 향상시킨다</li>
</ul>
</li>
<li><p><strong>데이터 변환의 차이</strong>:</p>
<ul>
<li><code>Scanner</code>는 다양한 기본형 데이터를 바로 변환(<code>nextInt()</code>, <code>nextDouble()</code> 등)할 수 있지만, <code>BufferedReader</code>는 <strong>String</strong> 형태로 읽어온 후 파싱(<code>Integer.parseInt()</code>, <code>Long.parseLong()</code>)이 필요하다</li>
</ul>
</li>
<li><p><strong>동기화 차이</strong>:</p>
<ul>
<li><code>Scanner</code>는 기본적으로 스레드 세이프(thread-safe)하여 느리지만, <code>BufferedReader</code>는 그렇지 않아 더 빠르다</li>
</ul>
</li>
</ol>
<hr />
<h2 id="💡-bufferedreader-기본-사용법">💡 BufferedReader 기본 사용법</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        System.out.println(&quot;입력값: &quot; + input);
        br.close();
    }
}</code></pre>
<h3 id="📝-코드-설명">📝 코드 설명</h3>
<ul>
<li><strong>입력</strong>: <code>readLine()</code> 메소드는 <strong>개행 문자</strong>까지 포함한 한 줄을 통째로 읽습니다.</li>
<li><strong>예외 처리</strong>: <code>IOException</code>을 꼭 처리해야 합니다.</li>
<li><strong>닫기</strong>: <code>BufferedReader</code>는 닫지 않으면 메모리 누수가 발생할 수 있습니다.</li>
</ul>
<hr />
<h2 id="⚡-stringbuilder란">⚡ StringBuilder란?</h2>
<p><strong>StringBuilder</strong>는 문자열을 효율적으로 다룰 수 있는 클래스입니다. 문자열의 추가, 수정, 삭제가 빈번한 경우 <strong>String</strong>보다 <strong>StringBuilder</strong>가 훨씬 빠릅니다.</p>
<h3 id="📌-주요-특징">📌 주요 특징</h3>
<ul>
<li><strong>가변 길이</strong>: 문자열을 동적으로 관리할 수 있습니다.</li>
<li><strong>메모리 효율성</strong>: <code>String</code>은 **불변(immutable)**이라서 매번 새로운 객체를 생성하지만, <strong>StringBuilder</strong>는 하나의 버퍼에서 데이터를 관리하여 메모리를 절약합니다.</li>
<li><strong>비동기성</strong>: 스레드 세이프하지 않지만, 그만큼 빠릅니다.</li>
</ul>
<h3 id="💡-stringbuilder-기본-사용법">💡 StringBuilder 기본 사용법</h3>
<pre><code class="language-java">public class Main {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        sb.append(&quot;Hello, &quot;);
        sb.append(&quot;World!&quot;);
        sb.append(&quot; 😊&quot;);
        System.out.println(sb.toString());
    }
}</code></pre>
<h3 id="📝-코드-설명-1">📝 코드 설명</h3>
<ul>
<li><strong>문자열 추가</strong>: <code>append()</code>를 사용하여 문자열을 이어붙입니다.</li>
<li><strong>최종 출력</strong>: <code>toString()</code>으로 최종 문자열을 반환합니다.</li>
<li><strong>빠른 출력</strong>: 여러 번의 <code>System.out.println()</code> 호출을 줄일 수 있습니다.</li>
</ul>
<hr />
<h2 id="🚀-bufferedreader--stringbuilder-예제-백준-15552번-빠른-ab">🚀 BufferedReader + StringBuilder 예제 (백준 15552번 빠른 A+B)</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i &lt; T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long A = Long.parseLong(st.nextToken());
            long B = Long.parseLong(st.nextToken());
            sb.append(A + B).append(&quot;\n&quot;);
        }
        System.out.print(sb.toString());
        br.close();
    }
}</code></pre>
<h3 id="📝-코드-설명-2">📝 코드 설명</h3>
<ul>
<li><strong>빠른 입력</strong>: <code>BufferedReader</code>로 줄 단위 입력 처리</li>
<li><strong>효율적 문자열 처리</strong>: <code>StringBuilder</code>로 결과 누적</li>
<li><strong>최종 출력 최적화</strong>: 여러 번의 출력 호출을 줄여 속도 개선</li>
</ul>