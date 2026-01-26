<h2 id="java-면접-질문-정리">Java 면접 질문 정리</h2>
<details>
  <b>1. JVM이 무엇인지, JVM의 구조와 JAVA의 실행방식을 설명해주세요.</b>
<br />

<h3 id="🧾-답변">🧾 답변</h3>
<p>JVM(Java Virtual Machine)은 자바 가상 머신의 약자이고 자바 애플리케이션을 클래스 로더를 통해 읽어 들여 자바 API와 함께 실행합니다. 그리고 Java와 OS 사이에서 중개자 역할을 수행하여 Java가 OS에 구애받지 않고 재사용을 가능하게 해줍니다. 또한 메모리 관리, Garbage collection을 수행합니다. <br />JVM의 구조는 Class Loader, Excetion engine, Runtime Data Area, JNI, Native Method Library로 이루어져 있습니다. <br /><strong>[자바 프로그램 실행 과정]</strong></p>
<ol>
<li>프로그램이 실행되면 JVM은 OS로부터 메모리를 할당한다. (JVM은 이 메모리를 용도에 따라 여러 영역으로 나누어 관리한다.)</li>
<li>자바 컴파일러(javac)가 자바 소스코드(.java)를 자바 바이트코드(.class)로 변환시킨다.</li>
<li>Class Loader를 통해 class파일들을 JVM으로 로딩한다.</li>
<li>로딩된 class파일들은 Execution engine을 통해 해석된다.</li>
<li>해석된 바이트코드는 Runtime Data Area에 배치되어 실질적인 수행이 이어지게 된다.
이러한 실행과정 속에서 JVM은 필요에 따라 Thread Synchronization과 GC같은 관리 작업을 수행한다.</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/53e89c1c-905f-4e54-a000-d2f3b890296b/image.png" /></p>
<br />
</details>

<hr />
<details>
  <b>2. GC가 무엇인지, 필요한 이유는 무엇인지, 동작방식에 대해 설명해주세요.</b>
<br />



<h3 id="🧾-답변-1">🧾 답변</h3>
<p>GC는 (Garbage Collection)으로 자바 이전에는 프로그래머가 모든 프로그램 메모리를 관리했지만, 자바에서는 JVM이 프로그램 메모리를 관리한다. <br />JVM은 가비지 컬렉션이라는 프로세스를 통해 메모리를 관리한다. 가비지 컬렉션은 자바 프로그램에서 사용되지 않는 메모리를 지속적으로 찾아내서 제거하는 역할을 한다. <br />[실행순서]
참조되지 않은 객체들을 탐색 후 삭제 -&gt; 삭제된 객체의 메모리 반환 -&gt; 힙 메모리 재사용</p>
<br />
</details>

<hr />
<details>
  <b>3. 컬렉션 프레임워크에 대해서 설명해주세요</b>
<br />


<h3 id="🧾-답변-2">🧾 답변</h3>
<p>Java Collection은 널리 알려져 있는 자료구조를 바탕으로 객체, 데이터들을 효율적으로 관리할 수 있는 자료구조들이 있는 라이브러리를 말한다.
왜 사용할까? 그 이유는 다수의 Data 를 다루는데 표준화된 클래스들을 제공해주기 때문에 DataStructure 를 직접 구현하지 않고 편하게 사용할 수 있기 때문이다. 또한 배열과 다르게 객체를 보관하기 위한 공간을 미리 정하지 않아도 되므로, 상황에 따라 객체의 수를 동적으로 정할 수 있다. 이는 프로그램의 공간적인 효율성 또한 높여준다.
List, Set은 Collection 인터페이스를 상속받지만, Map 인터페이스는 구조상의 차이라 별도로 정의한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/6fa920cd-fc48-487f-94c1-ea1fedc5f8ed/image.png" />
(초록색 박스는 인터페이스, 파란색 박스는 클래스를, 빨간 실선 화살표는 상속, 보라색 점선 화살표는 구현을 나타낸다.)</p>
<hr />
<h4 id="📌-list">📌 [List]</h4>
<p>List 컬렉션은 배열과 유사한 구조로 객체를 저장하게되면 각각의 주소에 인덱스가 부여되고 그 인덱스로 검색 삭제 기능을 제공할 수 있다.
순서를 가지고, 같은 객체의 중복저장이 가능하다.
대표적으로 ArrayList, LinkedList, Vector가 있다.</p>
<h4 id="📌-set">📌 [Set]</h4>
<p>Set 컬렉션은 집합형태의 구조를 가진다.
중복된 데이터를 저장 할 수 없고, 순서가 존재하지 않는다.
저장된 데이터를 인덱스로 관리하지 않기때문에 인덱스를 매개변수로 가지는 메서드가 존재하지 않는다.
대표적으로 순서가 없는 HashSet, 순서가 있는 TreeSet 클래스가 있다.</p>
<h4 id="📌-map">📌 [Map]</h4>
<p>Map 컬렉션은 Key와 Value로 구성된 Entry 객체를 저장하는 컬렉션이다.
이 때, Key의 객체는 중복될 수 없지만 Value의 객체는 중복될 수 있다.
Key로 객체를 관리하기때문에 대부분의 메서드의 파라미터로 Key를 가진다.
대표적으로 엔트리 순서를 보장하지 않는 HashMap와 HashTable, 순서를 가지는 TreeMap 클래스가 있다.</p>
<p>프로그래밍을 하다보면 간혹 수정할 수 없는(unmodifiable) 컬렉션을 생성해야 할 때가 있다.
List, Set, Map에서 생성하는경우 .of()나 .copyOf() 메서드를 상황에 맞게 사용할 수 있다.
배열을 List로 만들때 수정 할 수 없는 컬렉션을 생성하는경우 Arrays클래스의 .asList() 메서드를 사용할 수 있다.</p>
<br />
</details>

<hr />
<details>
  <b>4. 제네릭에 대해서 설명해주세요.</b>
<br />


<h3 id="🧾-답변-3">🧾 답변</h3>
<p>Generic은 자바의 타입 안정성을 맡고 있다. 컴파일 과정에서 타입체크를 해주는 기능으로 객체의 타입을 컴파일 시에 체크하기 때문에 객체의 타입 안정성을 높이고 형변환의 번거로움을 줄여준다.</p>
<hr />
<h4 id="📌-generic-사용법">📌 [Generic 사용법]</h4>
<p>컬렉션 클래스에서 타입 매개 변수로 사용하는 문자는 다른 변수와 혼동을 피하기 위해 일반적으로 하나의 대문자를 사용한다.
(표로 만들것)</p>
<ul>
<li> : Type </li>
<li> : Element</li>
<li> : Key</li>
<li> : Value</li>
<li> : Number</li>
</ul>
<pre><code class="language-java">public class ClassName &lt;T&gt; { ... }
public Interface InterfaceName &lt;T&gt; { ... }</code></pre>
<pre><code class="language-java">public class ClassName &lt;T, K&gt; { ... }
public Interface InterfaceName &lt;T, K&gt; { ... }

// HashMap의 경우
public class HashMap &lt;K, V&gt; { ... }</code></pre>
<pre><code class="language-java">public class MyClass &lt;T, K&gt; { ... }

public class Main {
    public static void main(String[] args) {
        MyClass&lt;String, Integer&gt; a = new MyClass&lt;Strnig, Integer&gt;();
    }
}</code></pre>
<p>생성된 제네릭 클래스를 사용여 객체를 생성할때, 구체적인 타입을 명시해주어야 한다.</p>
<br />
</details>

<hr />
<details>
  <b>5. 어노테이션에 대해서 설명해주세요.</b>
<br />

<h3 id="🧾-답변-4">🧾 답변</h3>
<p>어노테이션은 인터페이스를 기반으로 한 문법으로 주석처럼 코드에 달아 클래스에 특별한 의미를 부여하거나 기능을 주입할 수 있다.
JDK에 내장되어 있는 built-in annotation (대표적인 예, @Overrid)
어노테이션에 대한 정보를 나타내기 위한 어노테이션인 Meta annotation
개발자가 직접 만들어 내는 Custom annotation이 있다.
<br /></p>
</details>

<hr />
<details>
  <b>6. 오버라이딩과 오버로딩이 무엇이며 어떤 차이가 있을까요?</b>
<br />



<h3 id="🧾-답변-5">🧾 답변</h3>
<p>오버로딩의 경우에는 클래스 내에서 동일한 메소드 이름을 가지지만, 매개변수의 타입이나 개수를 다르게 구현할 수 있다.</p>
<pre><code class="language-java">main(blabla) {
  SuperClass object = new SubClass();
  fun(object);
}

fun(SuperClass super) {
  blabla....
}

fun(SubClass sub) {
  blabla....
}</code></pre>
<p>오버라이딩은 상위 클래스의 메소드를 하위 클래스에서 필요에 맞게 재정하는 것을 말한다.</p>
<br />
</details>

<hr />
<details>
  <b>7. 인터페이스와 추상클래스의 차이점에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-6">🧾 답변</h3>
<p>인터페이스는 구현 객체가 같은 동작을 한다는 것을 보장하기 위해 사용한다. 다중 상속이 가능하고, 인터페이스를 구현하는 집합간에는 관계가 없을 수 있다. (implements)
추상클래스는 객체의 추상적인 상위 개념으로 공통된 개념을 표현할 때 사용한다. 단일 상속만 가능하고 추상클래스를 상속하는 집합간에는 연관관계가 있다. (extends)</p>
<br />
</details>

<hr />
<details>
  <b>8. 클래스는 무엇이고 객체는 무엇인가요?</b>
<br />



<h3 id="🧾-답변-7">🧾 답변</h3>
<p>클래스는 객체를 정의하는 틀을 의미한다.
객체는 식별 가능한 개체를 의미한다. 객체는 구별 가능한 식별자, 특징적인 행동, 변경 가능한 상태를 가진다.</p>
<pre><code class="language-java">class Phone {
    //속성 정의
    String model;
    String color;
    int size;
    boolean isRecordingSupportive;

    //기능 정의
    void start() {
        System.out.println(&quot;전원을 켭니다&quot;);
    }

    void takePicture() {
        System.out.println(&quot;사진을 찍습니다.&quot;);
    }

    void makeCall() {
        System.out.println(&quot;전화를 겁니다.)&quot;
    }
}</code></pre>
<p>객체 지향 프로그래밍에서는 예제에서와 같은 객체를 추상화시켜 속성(state)과 기능(behavior)로 분류하여 각각 변수(variable)와 함수(function)으로 정의합니다.</p>
<br />
</details>

<hr />
<details>
  <b>9. 정적(static)이란 무엇인가요?</b>
<br />


<h3 id="🧾-답변-8">🧾 답변</h3>
<p>static은 클래스 멤버이고, 클래스 로더가 클래스를 로딩해서 메소드 메모리 영역에 적재할 떄 클래스별로 관리된다.
static 키워드를 통해 생성된 정적멤버들은 PermGen 또는 Metaspace에 저장되며 저장된 메모리는 모든 객체가 공유하며 하나의 멤버를 어디서든지 참조할 수 있는 장점이 있다.
그렇지만, GC의 관리 영역 밖에 존재하기 때문에 프로그램 종료시까지 메모리가 할당된채로 존재한다.</p>
<br />
</details>

<hr />
<details>
  <b>10. 자바의 원시타입들은 무엇이 있으며 각각 몇 바이트를 차지하나요?</b>
<br />



<h3 id="🧾-답변-9">🧾 답변</h3>
<p>boolean(1), char(unsigned 2), byte(1), short(2), int(4), long(8), float(4), double(8)</p>
<br />
</details>

<hr />
<details>
  <b>11. 접근 제어자의 종류와 이에 대해 설명해주세요. / Java의 Access Modifier의 4가지</b>
<br />



<h3 id="🧾-답변-10">🧾 답변</h3>
<p>변수 또는 메소드의 접근 범위를 설정해주기 위해 사용하는 Java의 예약어 4가지 private, default, protected, public
public
어떤 클래스에서라도 접근이 가능하다.</p>
<p>protected
클래스가 정의되어 있는 해당 패키지 내 그리고 해당 클래스를 상속받은 외부 패키지의 클래스에서 접근이 가능하다.</p>
<p>(default)
클래스가 정의되어 있는 해당 패키지 내에서만 접근이 가능하도록 접근 범위를 제한한다.</p>
<p>private
정의된 해당 클래스에서만 접근이 가능하도록 접근 범위를 제한한다.
<img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/2f50b808-01a8-42b5-acbd-81077e51aebc/image.png" /></p>
<br />
</details>

<hr />
<details>
  <b>12. 객체지향에 대해서 설명해주세요.</b>
<br />



<h3 id="🧾-답변-11">🧾 답변</h3>
<p>프로그래밍에서 필요한 데이터를 추상화시켜, 상태와 행위를 가진 객체로 만들고, 객체들의 유기적인 결합과 협력으로 파악하고자 하는 컴퓨터 프로그래밍을 말한다.
프로그램을 유연하고 변경이 용이하게 만들 수 있고 직관적인 코드 작성에 용이하다.</p>
<p>추상화(Abstraction): 객체의 공통적인 속성과 기능을 추출하여 정의하는 것
상속(Inheritance): 기존의 클래스를 재활용하여 새로운 클래스를 작성하는 자바 문법 요소
다형성(Polymorphism): 어떤 객체의 속성이나 기능이 상황에 따라 여러가지 형태를 가질 수 있는 성질
캡슐화(Encapsulation): 클래스 안에 서로 연관있는 속성과 기능들을 하나의 캡슐로 만들어 외부로부터 보호하는 것을 의미</p>
<br />
</details>

<hr />
<details>
  <b>13. SOLID(객체지향 5대원칙)에 대해서 설명해주세요.</b>
<br />



<h3 id="🧾-답변-12">🧾 답변</h3>
<p>SRP(단일책임원칙)은 한 클래스의 하나의 책임만 가져야 합니다.</p>
<p>OCP(개방-폐쇄 원칙)은 확장에는 열려 있으나 변경에는 닫혀 있어야 하며, 다형성을 활용해야 합니다.</p>
<p>LSP(리스코프 치환 원칙)은 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야하는 원칙으로 상위 타입을 상속해서 재정의 했을 때 프로그램이 깨지지 않아야 합니다.</p>
<p>ISP(인터페이스 분리 원칙)은 클라이언트는 자신이 사용하지 않는 메서드에 의존 관계를 맺으면 안되는 원칙입니다. 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 더 낫습니다. 즉, 비대한 인터페이스보단 더 작고 구체적인 인터페이스로 분리해야합니다.</p>
<p>DIP(의존관계 역전 원칙)은 추상적인 것은 자신보다 구체적인 것에 의존하지 않고, 변화하기 쉬운 것에 의존해서는 안된다는 원칙입니다. 구체적으론 구현 클래스에 의존하지 말고, 인터페이스에 의존해야 하는 원칙입니다.</p>
<br />
</details>

<hr />
<details>
  <b>14. 동일성(identity)와 동등성(equality)에 대해 설명해주세요. (equals(), ==)</b>
<br />



<h3 id="🧾-답변-13">🧾 답변</h3>
<p>동일성은 객체의 주소를 비교하는 것이고, 동등성은 객체의 같음을 비교하는 것이다.</p>
<p>기본적으로 자바에서는 Object 클래스에 정의된 equals() 메소드가 동일성 비교를 합니다. 따라서, 개발자는 원한다면 equals() 메소드를 오버라이딩해서 동등성의 판단 기준을 정의하면 된다.</p>
<br />
</details>

<hr />
<details>
  <b>15. String, StringBuilder, StringBuffer 각각의 차이에 대해 설명해주세요.</b>
<br />



<h3 id="🧾-답변-14">🧾 답변</h3>
<p>StringBuilder &gt; StringBuffer &gt;&gt;&gt; String</p>
<p>String은 불변이고 Garbage Collector로 제거되어야 한다.
객체가 불변하기 때문에 Multithread에서 동기화를 신경 쓸 필요가 없다.
StringBuilder와 StringBuffer은 이런 String 특징때문에 사용하는 가변타입이다.
StringBuilder와 StringBuffer는 Thread-safe 여부의 차이가 있다. StringBuilder는 Thread-safe하지 않다. 따라서 Multi-Thread 환경에서 사용할 때는 StringBuffer를 사용한다.
<img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/e466fe0a-9347-4d62-b421-e6c9a98d1235/image.png" /></p>
<p>buffer라는 공간을 통해 문자열을 바로 추가하기 때문에 공간 낭비가 없고 속도가 빠르다
<img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/33a80bb8-f8f7-49ea-afd8-50448077a256/image.png" />
주요 메서드에서 synchronized 키워드가 있기 때문에 멀티 스레드 환경에서 안전하다.
<img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/58a7cd99-520f-4e12-9622-562a8fcc4a77/image.png" /></p>
<br />
</details>

<hr />
<details>
  <b>16. Java8에서 추가된 기능에 대해서 설명해주세요.</b>
<br />



<h3 id="🧾-답변-15">🧾 답변</h3>
<p>Java8에서는 Lambda식, Stream API, Optional, 날짜 시간 API, StringJoiner 등이 추가되었습니다.</p>
<p>lambda는 함수형 프로그래밍을 지원하기 위한 기능이다.
Stream API는 고차함수를 지원한다.
Optional은 NullPointerExceptin을 방지하기 위해서 null 대신으로 나온 클래스로 Null-safety를 제공해, Stream과 사용법이 유사하다.
날짜 시간 API는 Joda-time등의 라이브러리에서 영향을 받았다.
StringJoiner는 문자열을 간단하게 구분자로 합칠 수 있는 기능을 제공한다.</p>
<br />
</details>

<hr />
<details>
  <b>17. try-with-resource에 대해서 설명해주세요.</b>
<br />



<h3 id="🧾-답변-16">🧾 답변</h3>
<p>AutoCloseable 인터페이스를 구현한 리소스에 대해 구문 종료시 자동으로 닫아주는 try문이다.
명시적으로 close하지 않아 코드가 간결하고, 예외가 발생하더라도 리소스가 정상적으로 닫히도록 보장한다.
외부 자원 사용 후 제대로 닫아줘서 메모리 누수가 없다.</p>
<pre><code class="language-java">package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

public class TryWithResource {

    public static void main(String[] args) {

        String inputFileName = &quot;input.txt&quot;;

        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                Objects.requireNonNull(Main.class.getClassLoader().getResourceAsStream(inputFileName))))) {

            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (NullPointerException e) {
            System.err.println(&quot;클래스패스에서 입력 파일을 찾을 수 없습니다: &quot; + inputFileName);
        } catch (IOException e) {
            System.err.println(&quot;파일 처리 중 오류 발생: &quot; + e.getMessage());
        }
    }
}</code></pre>
<br />
</details>

<hr />
<details>
  <b>18. 강한 결합과 느슨한 결합이 무엇인지 설명해주세요.</b>
<br />


<h3 id="🧾-답변-17">🧾 답변</h3>
<p>결합도는 의존성의 정도를 나타내고, 다른 모듈에 대해 얼마나 많은 정보를 알고 있는지에 대한 척도를 의미한다.
어떤 모듈이 다른 모듈에 너무 자세한 부분까지 알고 있을 경우에 강한 결합도를 가진다.
어떤 모듈이 다른 모듈에 대해 필요한 정보만 알고 있다면 두 모듈은 낮은 결합도를 가진다.
객체지향 관점에서 결합도는 객체 또는 클래스가 협력에 필요한 적절한 수준의 관계만을 유지하고 있는지를 나타냅니다. 이러한 관점에서 강한 결합도는 반드시 지양해야 하며, 개발자는 적절한 결합도를 유지할 수 있도록 고민하고 설계해야 합니다.</p>
<br />
</details>

<hr />
<details>
  <b>19. 직렬화와 역직렬화에 대해서 설명해주세요.</b>
<br />

<h3 id="🧾-답변-18">🧾 답변</h3>
<p>직렬화(Serialization)란 자바 시스템 내부에서 사용되는 객체 또는 데이터를 외부의 자바 시스템에서도 사용할 수 있도록 바이트 형태로 데이터 변환하는 기술과 변환된 데이터를 다시 변환하는 기술(역직렬화)을 말한다.</p>
<p>[직렬화 상황]
JVM에 상주하는 객체 데이터를 영속화할 때 사용
Servlet Session
Cache
Java RMI(Remote Method Invocation)</p>
<p>[직렬화 구현]</p>
<pre><code class="language-java">@Entity
@AllArgsConstructor
@toString
public class Post implements Serializable {
private static final long serialVersionUID = 1L;

private String title;
private String content;</code></pre>
<pre><code class="language-java">Post post = new Post(&quot;제목&quot;, &quot;내용&quot;);
byte[] serializedPost;
try (ByteArrayOutputStream baos = new ByteArrayOutputStream()) {
    try (ObjectOutputStream oos = new ObjectOutputStream(baos)) {
        oos.writeObject(post);

        serializedPost = baos.toByteArray();
    }
}</code></pre>
<p>[역직렬화 구현]</p>
<pre><code class="language-java">try (ByteArrayInputStream bais = new ByteArrayInputStream(serializedPost)) {
    try (ObjectInputStream ois = new ObjectInputStream(bais)) {

        Object objectPost = ois.readObject();
        Post post = (Post) objectPost;
    }
}</code></pre>
<br />
</details>

<hr />
<details>
  <b>20. Mutable 객체와 Immutable 객체의 차이점에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-19">🧾 답변</h3>
<p>Mutable은 객체가 변경 가능하다.
Immutable은 객체 생성 이후에는 객체의 상태가 바뀌지 않는 객체이다.
불변 객체 종류: String, Boolean,Integer,Float,Long 등
String을 제외하고 원시 타입의 wrapper 타입이다.</p>
<p>클래스들은 가변적이어야 하는 매우 타당한 이유가 있지 않는 한 반드시 불변으로 만들어야 한다. 만약 클래스를 불변으로 만드는 것이 불가능하다면, 가능한 변경 가능성을 최소화하라.</p>
<br />
</details>

<hr />
<details>
  <b>21. 자바에서 Null을 안전하게 다루는 방법에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-20">🧾 답변</h3>
<p>공개 메서드가 아닌 곳에는 assert를 사용하여 null을 방어할 수 있습니다.
또한 메서드의 인자를 받을 때 Objects.requireNonNull()을 사용하여 방어할 수 있습니다.
그리고 Optional을 사용해 리턴 타입에서 null을 반환하지 않도록 방어할 수 있습니다.</p>
<br />
</details>

<hr />
<details>
  <b>22. Java Build Tool에는 어떤것이 있으며, 그 중 Gradle에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-21">🧾 답변</h3>
<p>Java Build Tool은 소스 코드를 실행 가능한 애플리케이션으로 만들어주는 도구이고, 외부 라이브러리 자동 추가 및 관리가 가능하다
종류: APACHE ANT, Maven, Gradle</p>
<p>[ Gradle(그래들) ]
설정을 위해 Groovy(그루비) 문법을 사용한다.
외부 라이브러리를 관리할 수 있다.
유연하게 빌드 스크립트를 작성할 수 있다.
성능이 뛰어나다. (캐싱이 잘된다.)</p>
<p>기본으로 생성했을 때 Gradle 프로젝트 구조</p>
<pre><code class="language-java">├── build.gradle
├── .gradle
├── gradle 
│     └── wrapper 
│           ├── gradle-wrapper.jar 
│           └── gradle-wrapper.properties
├── gradlew 
├── gradlew.bat 
├── settings.gradle</code></pre>
<br />
</details>

<hr />
<details>
  <b>23. JAVA 컴파일 과정에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-22">🧾 답변</h3>
<p>컴파일이란? 소스코드를 컴퓨터가 이해할 수 있는 코드로 바꾸어주는 것이다.
목적코드를 실행파일로 바꾸는 것을 '링크'라고 한다.</p>
<p>[자바의 컴파일과 실행 과정]
<img alt="" src="https://velog.velcdn.com/images/hyeyun98/post/0d6dbce2-91f5-45ed-9f18-f8625502e1b6/image.png" /></p>
<ol>
<li>작성된 소스코드를 자바 컴파일러가 JVM이 이해할 수 있는 바이트코드로 변환한다.</li>
<li>컴파일된 바이트 코드를 JVM 내부의 클래스 로더가 가져와 동적 로딩을 통해 JVM 메모리상에 적재한다.</li>
<li>JVM 메모리에 적재된 바이트코드를 실행엔진을 통해 실행한다.</li>
</ol>
<br />
</details>

<hr />
<details>
  <b>24. 자바 메모리 관리 Xms, Xmx에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-23">🧾 답변</h3>
<p>자바 메모리 관리는 기본적으로 새로운 객체를 할당하고 적절하게 미사용 객체를 삭제하는 과정이다.</p>
<p>[Xms]
Xms(Initial Java Heap Size): JVM이 시작될 때 할당하는 최소 힙(heap) 크기를 지정한다.
힙은 자바 애플리케이션의 런타임 데이터, 객체 인스턴스 및 배열을 저장하는 메모리 영역이다.
Xms 옵션은 -Xms 형식으로 사용되며, 여기서 는 바이트 단위의 크기를 나타낸다.</p>
<p>[Xmx]
Xmx(Maximum Java Heap Size): JVM이 사용할 수 있는 최대 힙 크기를 지정한다.
애플리케이션의 메모리 요구 사항에 따라 힙 크기를 동적으로 조정하는 데 사용된다.
Xmx 옵션은 -Xmx 형식으로 사용되며, Xms와 마찬가지로 는 바이트 단위의 크기를 나타낸다.</p>
<br />
</details>

<hr />
<details>
  <b>25. Call by Value와 Call by Reference의 차이점에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-24">🧾 답변</h3>
<p>Call by Value는 함수의 인자를 전달할 때 값을 전달하는 방식이다.</p>
<pre><code class="language-java">public class MyClass {
    public static void main(String args[]) {
      int num1 = 10;
      int num2 = 20;

      System.out.println(&quot;Before Call Method : num1 = &quot; + num1 + &quot;, num2 = &quot; + num2);

      ex_method(num1, num2);

      System.out.println(&quot;After Call Method : num1 = &quot; + num1 + &quot;, num2 = &quot; + num2);
    }

    public static void ex_method(int num1, int num2) {
        num1 = 30;
        num2 = 40;

        System.out.println(&quot;Inside Method : num1 = &quot; + num1 + &quot;, num2 = &quot; + num2);

    }
}</code></pre>
<p>Call by Reference는 주소를 전달하는 방식이다.</p>
<pre><code class="language-java">public class MyClass {
    int value;

    MyClass(int value) {
        this.value = value;
    }

    public static void swap(MyClass x, MyClass y) {
        int temp = x.value;
        x.value = y.value;
        y.value = temp;

    }

    public static void main(String[] args) {

        MyClass num1 = new MyClass(10);
        MyClass num2 = new MyClass(20);


        System.out.println(&quot;Before Call Method : num1 = &quot; + num1.value + &quot;, num2 = &quot; + num2.value);

        swap(num1, num2);

        System.out.println(&quot;After Call Method : num1 = &quot; + num1.value + &quot;, num2 = &quot; + num2.value);

    }
}</code></pre>
<p>📌 자바는 Call by Value방식을 사용하며, Call by Reference는 존재하지 않는다.</p>
<p>[Java에서 Call by Reference는 없다면서?!]
자바의 데이터형에는 두가지가 있다.</p>
<p>기본형(primitive type) : Boolean Type(boolean), Numeric Type(short, int, long, float, double, char)
참조형(reference type) : Class Type, Interface Type, Array Type, Enum Type, 기본형을 제외한 모든 것들</p>
<p>기본형 (int, double, boolean 등)은 stack의 변수 안에 value 저장
참조형 (Integer, Obejct, Array, Map 등) 은 stakc의 변수 값에는 객체의 주소 값, 객체는 별도의 Heap영역에 저장</p>
<br />
</details>

<hr />
<details>
  <b>26. Stream API의 주요 기능과 3단계에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-25">🧾 답변</h3>
<p>Java의 Stream API는 개체 컬렉션을 처리하는 도구로 개발자가 간결하고 읽을 수 있는 코드로 컬렉션에 대한 복잡한 작업을 수행할 수 있다.
Stream API를 사용하면 기능적 프로그래밍 방식을 사용하여 데이터를 쉽게 필터링, 변환, 집계할 수 있다.
스트림은 병렬처리가 가능하도록 설계되었으므로 멀티 코어 프로세서를 활용하여 처리 속도를 높일 수 있다.</p>
<p>[Stream API의 특징]
원본의 데이터를 변경하지 않는다.
원본의 데이터를 조회하여 별도의 요소들로 stream을 생성한다.
원본의 데이터를 읽기만 하고, 정렬이나 필터링 등의 작업은 별도의 stream 요소들에서 처리가 된다.
일회용이다. 한번 사용하면 재사용이 불가능하다.
stream이 또 필요할 경우 다시 생성해주어야 한다.
내부 반복으로 작업을 처리한다.
기존에는 반복문을 사용하기 위해 for이나 while과 같은 문법을 사용해야 했지만, stream에서는 그런 문법을 메소드 내에 숨기고 있기 때문에, 보다 간결한 코드의 작성이 가능하다.
스트림의 연산은 필터(filter)-맵(map)기반의 API를 사요앟여 지연 연산을 통해 성능을 최적화 한다.
parallelStream() 메서드를 통한 손쉬운 병렬 처리를 지원한다.</p>
<p>[Stream API의 주요 기능]
Functional programming: 스트림은 함수형 프로그래밍 기술과 함께 사용되도록 설계 되어서 람다 식과 참조를 사용하여 집합에 대한 작업을 수행할 수 있다.
Lazy evaluation: 필요할 때만 스트림의 요소를 평가하여 메모리 사용량을 줄이고 성능을 향상시킬 수 있다.
Parallel processing: 병렬 처리가 가능하도록 설계되었으므로 멀티 코어 프로세서를 활용하여 처리 속도를 높일 수 있다.
Intermediate and terminal operations: 중간 및 종료의 두 가지 유형의 작업을 지원한다.
필터 및 맵과 같은 중간 작업은 추가로 처리할 수 있는 새 스트림을 반환한다. 종료 작업은 최종 결과를 생성한다.</p>
<p>[Stream API의 3가지 단계]</p>
<ol>
<li><p>생성하기
배열, 컬렉션, 임의의 수, 파일 등 거의 모든 것을 가지고 스트림을 생성할 수 있다.</p>
</li>
<li><p>가공하기
원본의 데이터를 별도의 데이터로 가공하기 위한 중간 연산의 단계.
어떤 객체의 stream을 원하는 형태로 처리할 수 있으며, 중간 연산의 반환값은 stream이기 때문에 필요한 만큼 중간 연사을 연결 할 수 있다.</p>
</li>
<li><p>결과 만들기
stream의 요소들을 소모하면서 연산이 수행되기 때문에 한번만 처리 가능하다.</p>
</li>
</ol>
<br />
</details>

<hr />
<details>
  <b>27. Lambda식에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-26">🧾 답변</h3>
<p>람다식이란 함수를 하나의 식으로 표현한 것이다.
함수를 람다식으로 표현하면 메소드의 이름이 필요없기 때문에 람다식은 익명함수의 한 종류라고 볼 수 있다.
기존 함수와는 다르게 메소드 명이 필요하지 않으며, 괄호()와 화살표 -&gt;를 이용해 함수를 선언하게 된다.
람다식이 등장하게 된 이유는 불필요한 코드를 줄이고, 가독성을 높이기 위함이다.</p>
<p>[람다식의 특징]</p>
<ol>
<li>람다식 내에서 사용되는 지역변수는 final이 붙지 않아도 상수로 간주된다.</li>
<li>람다식으로 선언된 변수명은 다른 변수명과 중복될 수 없다.</li>
</ol>
<p>[람다식의 장점]</p>
<ol>
<li>코드를 간결하게 만들 수 있다.</li>
<li>식에 개발자의 의도가 명확하게 드러나 가독성이 높아진다.</li>
<li>함수를 만드는 과정없이 한 번에 처리할 수 있어 생산성이 높아진다.</li>
<li>병렬프로그래밍이 용이하다.</li>
</ol>
<p>[람다식의 단점]</p>
<ol>
<li>람다를 사용하면서 만든 익명함수는 재사용이 불가능하다.</li>
<li>디버깅이 어렵다.</li>
<li>람다를 남발하면 비슷한 함수가 중복 생성되어 코드가 지저분해질 수 있다.</li>
<li>재귀로 만들경우 부적합하다.</li>
</ol>
<br />
</details>

<hr />
<details>
  <b>28. Java의 업캐스팅과 다운캐스팅에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-27">🧾 답변</h3>
<p>캐스팅(Casting)이란? 변수가 원하는 정보를 다 갖고 있는 것</p>
<p>[캐스팅이 필요한 이유는?]</p>
<ol>
<li>다형성: 오버라이딩된 함수를 분리해서 활용할 수 있다.</li>
<li>상속: 캐스팅을 통해 범용적인 프로그래밍이 가능하다.</li>
</ol>
<p>[형변환의 종류]</p>
<ol>
<li>묵시적 형변환: 캐스팅이 자동으로 발생 (업캐스팅)</li>
</ol>
<pre><code class="language-java">Parent p = new Child(); // (Parent) new Child()할 필요가 없음</code></pre>
<ol start="2">
<li>명시적 형변환: 캐스팅할 내용을 적어줘야 하는 경우 (다운캐스팅)</li>
</ol>
<pre><code class="language-java">Parent p = new Child();
Child c = (Child) p;</code></pre>
<br />
</details>

<hr />
<details>
  <b>29. Autoboxing/Unboxing이 성능에 미치는 영향을 설명하고 이를 최적화할 수 있는 방법을 설명해주세요.</b>
<br />

<h3 id="🧾-답변-28">🧾 답변</h3>
<p>Java에는 기본 타입과 Wrapper 클래스가 존재한다.
기본 타입 : int, long, float, double, boolean 등
Wrapper 클래스 : Integer, Long, Float, Double, Boolean  등</p>
<p>박싱: 기본 타입 데이터에 대응하는 Wrapper 클래스로 만드는 동작
언박싱: Wrapper 클래스에서 기본 타입으로 변환</p>
<p>JDK 1.5부터는 자바 컴파일러가 박싱과 언박싱이 필요한 상황에 자동으로 처리를 해준다.</p>
<pre><code class="language-java">// 오토 박싱
int i = 10;
Integer num = i;

// 오토 언박싱
Integer num = new Integer(10);
int i = num;</code></pre>
<br />
</details>

<hr />
<details>
  <b>30. Java에서의 Thread에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-29">🧾 답변</h3>
<p>모든 OS는 멀티태스킹을 지원한다.
동시에 처리될 수 있는 프로세스의 개수는 CPU코어의 개수와 동일한데, 이보다 많은 개수의 프로세스가 존재하기 때문에 모두 함께 동시에 처리할 수 없다.
멀티스레딩이란? 하나의 프로세스 안에 여러개의 스레드가 동시에 작업을 수행하는 것을 말하고, 스레드는 하나의 작업단위라고 생각하면 된다.</p>
<p>[스레드 구현 방법]</p>
<ol>
<li>Runnable 인터페이스 구현</li>
<li>Thread 클래스 상속</li>
</ol>
<p>[스레드 생성]
Runnable 인터페이스를 구현한 경우, 해당 클래스를 인스턴스화해서 Thread 생성자에 argument로 넘겨줘야 한다.
Thread 클래스를 상속받은 경우는, 상속받은 클래스 자체를 스레드로 사용할 수 있다.
또, Thread 클래스를 상속받으면 스레드 클래스의 메소드(getName())를 바로 사용할 수 있지만, Runnable 구현의 경우 Thread 클래스의 static 메소드인 currentThread()를 호출하여 현재 스레드에 대한 참조를 얻어와야만 호출이 가능하다.</p>
<p>[스레드 실행]
스레드의 실행은 run()호출이 아닌 start()호출로 해야한다.</p>
<p>[스레드의 실행제어]
스레드의 상태는 5가지가 있다</p>
<p>NEW : 스레드가 생성되고 아직 start()가 호출되지 않은 상태
RUNNABLE : 실행 중 또는 실행 가능 상태
BLOCKED : 동기화 블럭에 의해 일시정지된 상태(lock이 풀릴 때까지 기다림)
WAITING, TIME_WAITING : 실행가능하지 않은 일시정지 상태
TERMINATED : 스레드 작업이 종료된 상태</p>
<p>[동기화]
멀티스레드로 구현을 하다보면, 동기화는 필수다.
여러 스레드가 같은 프로세스 내의 자원을 공유하면서 작업할 때 서로의 작업이 다른 작업에 영향을 주기 때문이다
스레드의 동기화를 위해선, 임계 영역(critical section)과 잠금(lock)을 활용한다.
임계영역을 지정하고, 임계영역을 가지고 있는 lock을 단 하나의 스레드에게만 빌려주는 개념이다.
따라서 임계구역 안에서 수행할 코드가 완료되면, lock을 반납해줘야 한다.</p>
<p>[스레드 동기화 방법]
임계 영역(critical section) : 공유 자원에 단 하나의 스레드만 접근하도록(하나의 프로세스에 속한 스레드만 가능)
뮤텍스(mutex) : 공유 자원에 단 하나의 스레드만 접근하도록(서로 다른 프로세스에 속한 스레드도 가능)
이벤트(event) : 특정한 사건 발생을 다른 스레드에게 알림
세마포어(semaphore) : 한정된 개수의 자원을 여러 스레드가 사용하려고 할 때 접근 제한
대기 가능 타이머(waitable timer) : 특정 시간이 되면 대기 중이던 스레드 깨움</p>
<p>[synchronized 활용]
synchronized를 활용해 임계영역을 설정할 수 있다.</p>
<p>서로 다른 두 객체가 동기화를 하지 않은 메소드를 같이 오버라이딩해서 이용하면, 두 스레드가 동시에 진행되므로 원하는 출력 값을 얻지 못한다.</p>
<p>이때 오버라이딩되는 부모 클래스의 메소드에 synchronized 키워드로 임계영역을 설정해주면 해결할 수 있다.</p>
<pre><code class="language-java">//synchronized : 스레드의 동기화. 공유 자원에 lock
public synchronized void saveMoney(int save){    // 입금
    int m = money;
    try{
        Thread.sleep(2000);    // 지연시간 2초
    } catch (Exception e){

    }
    money = m + save;
    System.out.println(&quot;입금 처리&quot;);

}

public synchronized void minusMoney(int minus){    // 출금
    int m = money;
    try{
        Thread.sleep(3000);    // 지연시간 3초
    } catch (Exception e){

    }
    money = m - minus;
    System.out.println(&quot;출금 완료&quot;);
}</code></pre>
<br />
</details>

<hr />
<details>
  <b>31. Error와 Exception에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-30">🧾 답변</h3>
<p>프로그램이 실행 중 어떤 원인에 의해서 오작동을 하거나 비정상적으로 종료되는 경우를 프로그램 오류라고 하고, 프로그램 오류에는 에러(error)와 예외(exception) 두 가지로 구분할 수 있다.</p>
<p>Error 는 컴파일 시 문법적인 오류와 런타임 시 널포인트 참조와 같은 오류로 프로세스에 심각한 문제를 야기 시켜 프로세스를 종료 시킬 수 있다.</p>
<p>Exception 은 컴퓨터 시스템의 동작 도중 예기치 않았던 이상 상태가 발생하여 수행 중인 프로그램이 영향을 받는 것이다.</p>
<p>에러는 메모리 부족이나 스택오버플로우와 같이 발생하면 복구할 수 없는 심각한 오류이고, 예외는 발생하더라도 수습할 수 있는 덜 심각한 오류이다.</p>
<p>[Exception의 2가지 종류]
Checked Exception : 예외처리가 필수이며, 처리하지 않으면 컴파일되지 않습니다. JVM 외부와 통신(네트워크, 파일시스템 등)할 때 주로 쓰입니다.</p>
<p>RuntimeException 이외에 있는 모든 예외
IOException, SQLException 등</p>
<p>Unchecked Exception : 컴파일 때 체크되지 않고, Runtime에 발생하는 Exception을 말합니다.</p>
<p>RuntimeException 하위의 모든 예외
NullPointerException, IndexOutOfBoundException 등</p>
<p>[예외 관련 2가지]</p>
<ol>
<li>try ~ catch 구문</li>
<li>throws 구문</li>
</ol>
<br />
</details>

<hr />
<details>
  <b>32. Java의 Record에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-31">🧾 답변</h3>
<p>Java 14버전부터 도입되고 16부터 정식 스펙에 포함된 Record는 class처럼 타입으로 사용이 가능하다.</p>
<p>보통 Entity나 DTO 구현에 있어서 많이 사용하는 형식이다.</p>
<pre><code class="language-java">public record Person(
    String name,
    int age
) {}</code></pre>
<p>자동으로 필드를 private final로 선언하여 만들어주고, 생성자와 getter까지 암묵적으로 생성된다.
또한 equals, hasCode, toSring도 자동으로 생성된다.</p>
<br />
</details>

<hr />
<details>
  <b>33. Java의 Primitive type과 Reference type에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-32">🧾 답변</h3>
<p>Java에는 기본형(Primitive type)과 참조형(Reference type)이 있다.</p>
<pre><code class="language-java">Java Data Type 
ㄴ Primitive Type
    ㄴ Boolean Type(boolean)
    ㄴ Numeric Type
        ㄴ Integral Type
            ㄴ Integer Type(short, int, long)
            ㄴ Floating Point Type(float, double)
        ㄴ Character Type(char)
ㄴ Reference Type
    ㄴ Class Type
    ㄴ Interface Type
    ㄴ Array Type
    ㄴ Enum Type
    ㄴ etc.</code></pre>
<p>[Primitive type] 기본형 타입
JAVA에서는 총 8가지의 Primitive type을 미리 정의하고 제공합니다.
자바에서 기본 자료형은 반드시 사용하기 전에 선언(Declared)되어야 합니다.
OS에 따라 자료형의 길이가 변하지 않습니다.
비객체 타입입니다. 따라서 null 값을 가질 수 없습니다. 만약 Primitive type에 Null을 넣고 싶다면 Wrapper Class를 활용합니다.
스택(Stack) 메모리에 저장됩니다.</p>
<p>boolean, char, byte, short, int, long, float, double</p>
<p>[Reference type] 참조형 타입
JAVA에서 Primitive type을 제외한 타입들이 모두 Reference type 입니다.
Reference type은 JAVA에서 최상인 java.lang.Object클래스를 상속하는 모든 클래스들을 말합니다. 물론 new로 인하여 생성하는 것들은 메모리 영역인 Heap 영역에 생성을 하게되고, Garbage Collector가 돌면서 메모리를 해제합니다.
클래스 타입(class type) , 인터페이스 타입(interface type) , 배열 타입(array type) , 열거 타입(enum type) 이 있습니다.
빈 객체를 의미하는 Null이 존재합니다.
문법상으로는 에러가 없지만 실행시켰을 때 에러가 나는 런타임 에러가 발생합니다. 예를 들어 객체나 배열을 Null 값으로 받으면 NullPointException이 발생하므로 변수 값을 넣어야 합니다.
Heap 메모리에 생성된 인스턴스는 메소드나 각종 인터페이스에서 접근하기 위해 JVM의 Stack 영역에 존재하는 Frame에 일종의 포인터(C의 포인터와는 다릅니다.)인 참조값을 가지고 있어 이를 통해 인스턴스를 핸들링합니다.</p>
<br />
</details>

<hr />
<details>
  <b>34. Java의 Composition에 대해 설명해주세요.</b>
<br />


<h3 id="🧾-답변-33">🧾 답변</h3>
<p>Composition이란 기존 클래스가 새로운 클래스의 구성요소가 되는 것이다.
상속의 단점을 커버할 수 있다.</p>
<p>[상속의 단점]</p>
<ol>
<li>캡슐화 위반</li>
<li>유연하지 못한 설계</li>
<li>다중상속 불가능</li>
</ol>
<p>Composition은 상속처럼 기존의 클래스를 확장(extend)하는 것이 아닌, 새로운 클래스를 생성하여 private 필드로 기존 클래스의 인스턴스를 참조하는 방식이다. (forwarding)이라고도 부른다.</p>
<p>새로운 클래스이기 때문에, 여기서 어떠한 생성 작업이 일어나더라도 기존의 클래스는 전혀 영향을 받지 않는다는 점이 핵심이다.</p>
<br />
</details>

<hr />
<details>
  <b>35. 직렬화에서 SerialVersionUID를 선언해야 하는 이유를 설명해주세요.</b>
<br />


<h3 id="🧾-답변-34">🧾 답변</h3>
<p>Serializable을 상속하는 클래스의 경우 버저닝을 위해 serialVersionUID 변수를 사용한다. 이때 명시적으로 지정하지 않으면 컴파일러가 계산한 값을 부여하는데, 컴파일러에 따라 할당되는 값이 다를 수 있어 동일 버전임에도 다른 버전으로 취급할 수 있다.
값이 따르면 역직렬화 시 InvalidClassException이 발생하여 이슈가 발생한다.</p>
<br />
</details>

<hr />
<details>
  <b>36. 자바의 동시성 이슈(공유자원 접근)에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-35">🧾 답변</h3>
<p>자바의 동시성 이슈는 여러 스레드가 같은 데이터를 동시에 건드릴 때 값이 엉키거나(경쟁), 한쪽에서 바뀐 것이 다른 쪽에 바로 보이지 않는(가시성) 문제입니다.</p>
<p>[해결방법]</p>
<ul>
<li>synchronized나 ReentrantLock으로 임계 영역을 보호</li>
<li>Atomic 타입/volatile을 상황에 맞게 사용</li>
<li>데드락을 피하기 위한 락 설계와 동기화 범위 최소화</li>
<li>가능한 불변(immutable) 객체로 설계</li>
</ul>
<br />
</details>

<hr />
<details>
  <b>37. Volatile 키워드에 대해 설명해주세요.</b>
<br />

<h3 id="🧾-답변-36">🧾 답변</h3>
<p>[가시성 보장]</p>
<ul>
<li><p>자바에서 스레드는 성능을 높이기 위해 주 메모리 (힙과 같이 모든 스레드가 공유하는 메모리) 에 대해 로컬 메모리(CPU 레지스터 또는 캐시) 에 복사해서 작업합니다.
이후 작업이 끝나면 주 메모리에 기록합니다.
따라서 다른 스레드가 주 메모리에 기록하기 전에는 최신값을 보지 못합니다.
volatile 으로 선언하면, 모든 쓰기와 읽기가 주 메모리에서 이루어집니다.</p>
</li>
<li><p>자바에서는 성능 최적화를 위해 프로그램의 최종 결과에 영향을 주지 않는 범위에서 명령어를 재정렬합니다. 이는 명령어 재정렬이 가시성 보장을 하지 않게 합니다.</p>
</li>
<li><p><strong>객체 생성 과정의 3단계 (이 중에 2,3 단계가 재정렬될 수 있어서, 다른 스레드에서 초기화 되지 않은 객체의 변수에 접근할 수 있음)</strong></p>
</li>
<li><p>1단계: 메모리 할당</p>
</li>
<li><p>2단계: 생성자 호출로 객체 초기화</p>
</li>
<li><p>3단계: 객체 참조를 변수에 할당 (<code>instance</code>에 연결)</p>
</li>
</ul>
<br />
</details>

<hr />
<details>
  <b>38. new String(..)과 리터럴 문자열의 차이점을 설명해주세요.</b>
<br />


<h3 id="🧾-답변-37">🧾 답변</h3>
<ul>
<li>리터럴은 String Pool 에 저장되는 불변 객체입니다.</li>
<li>String 은 Heap 영역에 저장되고 리터럴 문자 모두 Heap 메모리에 위치합니다. 따라서 String Pool 도 GC 의 영향을 받아 메모리에서 제거될 수 있습니다. (다만 Java 7 미만 버전에서는 메소드 영역에 위치했습니다)</li>
<li>String Pool 은 이미 동일한 문자열이 존재하는 경우 pool 에 있는 객체를 사용해서 메모리 절약과 속도 향상이 있다.</li>
</ul>
<br />
</details>

<hr />