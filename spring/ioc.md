## IoC — Inversion of Control

**IoC means Spring takes control of creating and managing objects instead of the application creating them directly.**

Without Spring:

```java
Specification specification = new Specification();
Car car = new Car(specification);
```

With Spring:

```java
Car myCar = (Car) context.getBean("myCar");
```

The Spring container creates and wires the required objects.

### IoC example

Two providers are registered:

```xml
<bean id="userDatabaseProvider"
      class="com.ioc.coupling.UserDatabaseProvider"/>

<bean id="webServiceProvider"
      class="com.ioc.coupling.WebServiceProvider"/>
```

Two `UserManager` objects are then created with different providers:

```xml
<bean id="userManagerWithDataProvider"
      class="com.ioc.coupling.UserManager">
    <constructor-arg ref="userDatabaseProvider"/>
</bean>

<bean id="userManagerWithWSProvider"
      class="com.ioc.coupling.UserManager">
    <constructor-arg ref="webServiceProvider"/>
</bean>
```

The application only asks Spring for the required object:

```java
UserManager userManagerWithDB =
        (UserManager) context.getBean("userManagerWithDataProvider");

UserManager userManagerWithWS =
        (UserManager) context.getBean("userManagerWithWSProvider");
```

**Key idea:** The application says **what it needs**; Spring handles **how it is created and connected**.