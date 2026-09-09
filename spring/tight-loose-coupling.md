# Tight vs Loose Coupling in Spring Boot

## 1. What is Coupling?

**Coupling** = how strongly one class depends on another class.

- **Tight coupling:** A class directly creates/depends on a specific implementation.
- **Loose coupling:** A class depends on an abstraction (interface), and the implementation is provided from outside.

---

## 2. Tight Coupling

### Example

```java
public class UserManager {
    UserDatabase userDatabase = new UserDatabase();

    public String getUserInfo(){
        return userDatabase.getUserDetails();
    }
}
```

```java
public class UserDatabase {
    public String getUserDetails(){
        return "User Details from Database";
    }
}
```

### Why is it tightly coupled?

`UserManager` directly creates `UserDatabase`:

```java
UserDatabase userDatabase = new UserDatabase();
```

So `UserManager` knows:
- The exact implementation: `UserDatabase`
- How to create it: `new UserDatabase()`

If we want to replace the database with another provider, `UserManager` must be changed.

**Problem:**
```text
UserManager → UserDatabase
              (direct dependency)
```

---

## 3. Loose Coupling

### Example

First, define an interface:

```java
public interface UserDataProvider {
    String getUserDetails();
}
```

Implementation:

```java
public class UserDatabaseProvider implements UserDataProvider {

    @Override
    public String getUserDetails(){
        return "User Details from Database";
    }
}
```

`UserManager` depends only on the interface:

```java
public class UserManager {
    private UserDataProvider userDataProvider;

    public UserManager(UserDataProvider userDataProvider){
        this.userDataProvider = userDataProvider;
    }

    public String getUserInfo(){
        return userDataProvider.getUserDetails();
    }
}
```

### Why is it loosely coupled?

`UserManager` does **not** create `UserDatabaseProvider`.

It only knows about:

```java
UserDataProvider
```

The actual implementation is supplied through the constructor.

```text
                 ┌→ UserDatabaseProvider
UserManager → UserDataProvider
                 └→ AnotherProvider
```

So the implementation can be changed without modifying `UserManager`.

---

## 4. How Spring Boot Makes This Easier

Spring Boot uses **Dependency Injection (DI)** to provide dependencies.

For example:

```java
@Component
public class UserDatabaseProvider implements UserDataProvider {
    ...
}
```

```java
@Service
public class UserManager {

    private final UserDataProvider userDataProvider;

    public UserManager(UserDataProvider userDataProvider) {
        this.userDataProvider = userDataProvider;
    }
}
```

Spring creates `UserDatabaseProvider` and injects it into `UserManager`.

This is **Constructor Injection**.

```text
Spring Container
      │
      ├── creates UserDatabaseProvider
      │
      └── injects it into
              ↓
         UserManager
```

---

## 5. Key Difference

| Tight Coupling | Loose Coupling |
|---|---|
| Depends on concrete class | Depends on interface/abstraction |
| Uses `new` to create dependency | Dependency is injected |
| Harder to replace implementation | Easy to replace implementation |
| Harder to unit test | Easier to mock/test |
| Less flexible | More flexible |

### Interview Answer

> **Tight coupling** means a class directly depends on and creates a specific implementation. **Loose coupling** means a class depends on an abstraction, such as an interface, and the actual implementation is provided externally through Dependency Injection.

**Remember:**  
`new` inside a class → usually tighter coupling  
Interface + Dependency Injection → loose coupling