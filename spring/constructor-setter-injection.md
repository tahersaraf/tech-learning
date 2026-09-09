## Dependency Injection (DI)

**Dependency Injection is the mechanism Spring uses to provide an object's dependencies.**

Example:

`Car` depends on `Specification`.

```java
public class Car {
    private Specification specification;
}
```

Instead of `Car` creating `Specification`, Spring provides it.

### Constructor Injection

Dependency is provided through the constructor.

`Car`:

```java
public class Car {
    private Specification specification;

    public Car(Specification specification) {
        this.specification = specification;
    }
}
```

XML:

```xml
<bean id="carSpecification"
      class="car.example.constructor.injection.Specification">
    <property name="make" value="Toyota"/>
    <property name="model" value="Corolla"/>
</bean>

<bean id="myCar"
      class="car.example.constructor.injection.Car">
    <constructor-arg ref="carSpecification"/>
</bean>
```

**Flow:**

`Specification Bean → constructor-arg → Car constructor → Car gets Specification`

### Why Constructor Injection?

- Dependency is available when the object is created.
- Good for **required dependencies**.
- Makes the dependency explicit.
- Supports immutable/final dependencies when designed that way.


## Setter Injection

Dependency is provided through a setter method.

`Car`:

```java
public class Car {
    private Specification specification;

    public void setSpecification(Specification specification) {
        this.specification = specification;
    }
}
```

XML:

```xml
<bean id="carSpecification"
      class="car.example.setter.injection.Specification">
    <property name="make" value="Toyota"/>
    <property name="model" value="Corolla"/>
</bean>

<bean id="myCar"
      class="car.example.setter.injection.Car">
    <property name="specification" ref="carSpecification"/>
</bean>
```

**Flow:**

`Specification Bean → property ref → setSpecification() → Car gets Specification`

### When to use?

- Useful for **optional dependencies**.
- Dependency can be changed after object creation.
- Requires a setter.


## Constructor vs Setter Injection

| | Constructor Injection | Setter Injection |
|---|---|---|
| Injection point | Constructor | Setter method |
| Dependency available | At object creation | After object creation |
| Best suited for | Required dependencies | Optional dependencies |
| Immutability | Easier | Harder |
| Your XML | `<constructor-arg ref="..."/>` | `<property name="..." ref="..."/>` |

---