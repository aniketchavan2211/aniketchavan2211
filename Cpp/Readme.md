## Cpp (C++)

### Comments

Comments are ignored by C compiler, Programmer use to write description of code.
we comment code that should not execute but remain in code.

#### Single-line Comments

`//` is used for single line comment

```cpp
#include <iostream>
using namespace std;

int main() {
  cout << "Hello" << endl; // World
  return 0;
}

// Hello World
```

here World and Hello World is ignored by compiler,
it not throw an error or print on screen.


#### Multi-line Comments

What if we want to comment more than 15 line of code.
At begining of Multi-line Comments `/*`
and at end `*/`

**Syntax:**
```cpp
int main() {
  /*  Multi-line
  Comments */
  return 0;
}
```

here. Multi-line comment is ignored.
two line of code are ignored.
