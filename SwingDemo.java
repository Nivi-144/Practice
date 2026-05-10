import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class SwingDemo extends JFrame implements ActionListener {
    // Components
    JTextField textField;
    JButton button;
    JLabel label;
    // Constructor
    SwingDemo() {
        // Frame title
        setTitle("Swing Demo");
        // Layout Manager
        setLayout(new FlowLayout());
        // Create components
        textField = new JTextField(20);
        button = new JButton("Display");
        label = new JLabel("Enter text and click button");
        // Add action listener to button
        button.addActionListener(this);
        // Add components to frame
        add(textField);
        add(button);
        add(label);
        // Frame settings
        setSize(400, 200);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    // Event handling method
    public void actionPerformed(ActionEvent e) {
        // Get text from text field
        String text = textField.getText();
        // Display text in label
        label.setText("You entered: " + text);
    }
    // Main method
    public static void main(String[] args) {
        new SwingDemo();
    }
}
