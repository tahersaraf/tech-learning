## Spring Bean

A **Bean** is an object created, configured, and managed by the Spring IoC container.

### Hands-on example

`MyBean` is a simple Java class:

```java
public class MyBean {
    private String message;

    public void setMessage(String message) {
        this.message = message;
    }

    public void showMessage(){
        System.out.println("Message: " + message);
    }

    @Override
    public String toString() {
        return "MyBean{" +
                "message='" + message + '\'' +
                '}';
    }
}
```

Bean definition in `applicationBeanContext.xml`:

```xml
<bean id="myBean" class="car.example.bean.MyBean">
    <property name="message" value="This is my first bean"/>
</bean>
```

Spring creates the `MyBean` object and injects `"This is my first bean"` through the setter.

Retrieve the Bean:

```java
ApplicationContext context =
        new ClassPathXmlApplicationContext("applicationBeanContext.xml");

MyBean myBean = (MyBean) context.getBean("myBean");
System.out.println(myBean);
```

**Flow:**

`XML configuration → Spring IoC Container → Bean creation → Property injection → getBean()`
