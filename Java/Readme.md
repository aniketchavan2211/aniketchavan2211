## Java


### Hello World
```java

public Hello
{
  public static void main(String[] args)
  {
    System.out.println("Hello, World \n ");
  }
}
```

To Compile to `.class`
```bash
ecj Hello.java
```

Then to .class convert to `dexfile.dex`
```bash
dx --dex --output=hello.dex Hello.class
```

Run in Dalvikvm 
```bash
dalvikvm -cp hello.dex Hello
```
