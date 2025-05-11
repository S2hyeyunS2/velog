<p>Java를 사용하다 보면 <code>int</code>와 <code>Integer</code>의 차이점을 헷갈릴 때가 많았다!!</p>
<hr />
<h2 id="📚-차이점">📚 차이점</h2>
<table>
<thead>
<tr>
<th>특징</th>
<th>int (Primitive Type)</th>
<th>Integer (Wrapper Class)</th>
</tr>
</thead>
<tbody><tr>
<td>메모리 크기</td>
<td>4 bytes</td>
<td>약 16 bytes (객체 오버헤드 포함)</td>
</tr>
<tr>
<td>기본값</td>
<td>0</td>
<td>null (객체이므로 초기화하지 않으면 null)</td>
</tr>
<tr>
<td>Null 허용 여부</td>
<td>❌ (불가능)</td>
<td>✅ (가능)</td>
</tr>
<tr>
<td>사용 사례</td>
<td>기본적인 산술 연산</td>
<td>컬렉션, 제네릭스, 데이터베이스 매핑</td>
</tr>
<tr>
<td>Autoboxing/Unboxing</td>
<td>❌</td>
<td>✅</td>
</tr>
</tbody></table>
<p><code>int</code>는 기본형(primitive type)으로, 값만 저장하며 메모리를 효율적으로 사용
반면 <code>Integer</code>는 객체(reference type)로, 추가적인 메모리와 객체 생성 </p>
<hr />
<h2 id="🔍-메모리-구조">🔍 메모리 구조</h2>
<ul>
<li><p><strong>int (Primitive)</strong></p>
<ul>
<li>기본 데이터 타입으로 스택(stack) 메모리에 저장</li>
<li>메모리 사용량이 작고, garbage collection의 영향을 받지 않음</li>
</ul>
</li>
<li><p><strong>Integer (Wrapper)</strong></p>
<ul>
<li>객체로 힙(heap) 메모리에 저장되며, 참조(reference) 주소를 통해 접근</li>
<li>내부적으로 <code>int</code> 값을 저장하지만 객체 오버헤드가 있어 더 많은 메모리를 차지</li>
</ul>
</li>
</ul>
<hr />
<h2 id="📝-autoboxing과-unboxing">📝 Autoboxing과 Unboxing</h2>
<p><code>Integer</code>와 <code>int</code>는 자바의 자동 변환 기능을 통해 상호 변환될 수 있음</p>
<h3 id="autoboxing-기본형---래퍼-클래스">Autoboxing (기본형 -&gt; 래퍼 클래스)</h3>
<pre><code class="language-java">int num = 5;
Integer boxedNum = num; // Autoboxing</code></pre>
<h3 id="unboxing-래퍼-클래스---기본형">Unboxing (래퍼 클래스 -&gt; 기본형)</h3>
<pre><code class="language-java">Integer wrappedNum = 10;
int unboxedNum = wrappedNum; // Unboxing</code></pre>
<p>이 기능은 편리하지만, 불필요한 Autoboxing/Unboxing은 성능 저하의 원인이 될 수 있다</p>
<hr />
<h2 id="🛠-사용-사례와-주의점">🛠 사용 사례와 주의점</h2>
<h3 id="1-데이터베이스-매핑-jpa">1. 데이터베이스 매핑 (JPA)</h3>
<p>JPA를 사용하여 엔티티를 정의할 때, 데이터베이스 테이블의 컬럼과 자바 필드를 매핑해야 함
이때, <strong>nullable</strong>한 필드는 반드시 <code>Integer</code>를 사용!!</p>
<pre><code class="language-java">public record UpdateItemRequest(
        @NotBlank(message = &quot;상품명은 필수 항목입니다.&quot;)
        String name,

        @PositiveOrZero(message = &quot;상품 가격은 0원 이상이어야 합니다.&quot;)
        @NotNull(message = &quot;상품 가격은 필수 항목입니다.&quot;)
        Integer price,

        @PositiveOrZero(message = &quot;상품 수량은 0개 이상이어야 합니다.&quot;)
        @NotNull(message = &quot;상품 수량은 필수 항목입니다.&quot;)
        Integer quantity,

        @Min(value = 0, message = &quot;상품 할인율은 0% 이상이어야 합니다.&quot;)
        @Max(value = 100, message = &quot;상품 할인율은 100% 이하어야 합니다.&quot;)
        int discount,

        @NotNull(message = &quot;최대 주문 수량은 필수 항목입니다.&quot;)
        Integer maxBuyQuantity,

        String description,
        Long mainCategoryId,
        Long subCategoryId
) {}</code></pre>
<ul>
<li><p><strong>왜 Integer를 사용했는가?</strong></p>
<ul>
<li><code>discount</code>는 기본값이 0으로 충분히 의미가 명확하여 <code>int</code>를 사용</li>
</ul>
</li>
</ul>
<h3 id="2-컬렉션-및-제네릭">2. 컬렉션 및 제네릭</h3>
<p>기본형(<code>int</code>)은 제네릭 타입의 컬렉션(<code>List</code>, <code>Set</code>, <code>Map</code>)에서 직접 사용할 수 없음</p>
<pre><code class="language-java">List&lt;Integer&gt; numbers = new ArrayList&lt;&gt;();
numbers.add(5); // 가능

// List&lt;int&gt;는 불가능</code></pre>
<h3 id="3-기본값-처리">3. 기본값 처리</h3>
<ul>
<li><strong>int</strong>: 기본값이 0이므로 초기화되지 않은 상태와 실제 0의 의미가 혼동될 수 있다</li>
<li><strong>Integer</strong>: 기본값이 <code>null</code>이므로 초기화되지 않은 상태를 명확히 표현할 수 있다.</li>
</ul>
<h3 id="4-nullpointerexception-위험성">4. NullPointerException 위험성</h3>
<ul>
<li><code>Integer</code>를 사용하면 <code>null</code>을 허용할 수 있지만, <code>null</code>을 참조할 때 <code>NullPointerException</code>이 발생할 수 있다</li>
<li>이 문제는 특히 데이터베이스에서 값이 없는 경우, 또는 REST API에서 필드가 누락된 경우에 자주 발생할 수 있다</li>
</ul>
<hr />
<h2 id="🚀-최적화-포인트">🚀 최적화 포인트</h2>
<ul>
<li><p><strong>메모리 최적화</strong></p>
<ul>
<li><code>int</code>는 더 작고 빠르지만, <code>null</code>을 다룰 필요가 없는 경우에만 사용</li>
</ul>
</li>
<li><p><strong>성능 고려</strong></p>
<ul>
<li><code>Integer</code>를 자주 생성하거나 해제하면 메모리와 성능에 영향을 줄 수 있다</li>
</ul>
</li>
</ul>
<hr />
<h2 id="📌-결론">📌 결론</h2>
<ul>
<li><p>기본적으로 <code>int</code>를 사용하되, 다음과 같은 경우에는 <code>Integer</code>를 사용</p>
<ul>
<li>데이터베이스에서 <code>null</code> 허용 필드</li>
<li>제네릭 컬렉션</li>
<li><code>null</code> 초기화가 필요한 경우</li>
</ul>
</li>
</ul>