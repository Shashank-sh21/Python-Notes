#include <Servo.h>

// Motor pins
const int motorA1 = 3; // Motor A forward
const int motorA2 = 4; // Motor A backward
const int motorB1 = 5; // Motor B forward
const int motorB2 = 6; // Motor B backward

// Servo pin
const int servoPin = 9;

// Create Servo object
Servo gripper;

// Function to move forward
void moveForward(int duration) {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
  delay(duration);
  stopMotors();
}

// Function to stop motors
void stopMotors() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}

// Function to open gripper
void openGripper() {
  gripper.write(0); // Adjust angle as needed for opening
  delay(1000); // Wait for the gripper to open
}

// Function to close gripper
void closeGripper() {
  gripper.write(90); // Adjust angle as needed for closing
  delay(1000); // Wait for the gripper to close
}

void setup() {
  // Set motor pins as output
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);

  // Attach the servo to the pin
  gripper.attach(servoPin);
  
  // Initialize gripper
  openGripper();
}

void loop() {
  // Move to the pick position
  moveForward(2000); // Move forward for 2 seconds
  
  // Pick the object
  closeGripper(); // Close the gripper to pick the object
  
  // Move to the place position
  moveForward(2000); // Move forward for 2 seconds
  
  // Place the object
  openGripper(); // Open the gripper to release the object
  
  // Stop for a while before repeating
  delay(2000);
}