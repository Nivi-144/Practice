class Student {
    // Private variables (data hiding)
    private String name;
    private int age;

    // Setter method (to set values)
    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        if(age > 0) {   // validation
            this.age = age;
        }
    }

    // Getter method (to get values)
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student();

        // Setting values using setters
        s.setName("Nivedita");
        s.setAge(20);

        // Getting values using getters
        System.out.println("Name: " + s.getName());
        System.out.println("Age: " + s.getAge());
    }
}
