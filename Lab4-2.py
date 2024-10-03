#include <stdio.h>

// Function prototypes
float celsius_to_fahrenheit(float celsius);
float fahrenheit_to_celsius(float fahrenheit);
float celsius_to_kelvin(float celsius);
float kelvin_to_celsius(float kelvin);
float fahrenheit_to_kelvin(float fahrenheit);
float kelvin_to_fahrenheit(float kelvin);
void categorize_temperature(float celsius);
void temperature_conversion();

// Main function
int main() {
    temperature_conversion();
    return 0;
}

// Function to handle the temperature conversion process
void temperature_conversion() {
    float temperature;
    int current_scale, target_scale;
    float converted_temp;

    // Input temperature
    printf("Enter the temperature: ");
    if (scanf("%f", &temperature) != 1) {
        printf("Invalid input. Please enter a numeric value.\n");
        return;
    }

    // Input current scale
    printf("Choose the current scale (1) Celsius, (2) Fahrenheit, (3) Kelvin: ");
    if (scanf("%d", &current_scale) != 1 || current_scale < 1 || current_scale > 3) {
        printf("Invalid input. Please choose 1, 2, or 3.\n");
        return;
    }

    // Input target scale
    printf("Convert to (1) Celsius, (2) Fahrenheit, (3) Kelvin: ");
    if (scanf("%d", &target_scale) != 1 || target_scale < 1 || target_scale > 3) {
        printf("Invalid input. Please choose 1, 2, or 3.\n");
        return;
    }

    // Conversion logic
    if (current_scale == 1) { // Celsius
        if (target_scale == 2) converted_temp = celsius_to_fahrenheit(temperature);
        else if (target_scale == 3) converted_temp = celsius_to_kelvin(temperature);
        else converted_temp = temperature;
    } else if (current_scale == 2) { // Fahrenheit
        if (target_scale == 1) converted_temp = fahrenheit_to_celsius(temperature);
        else if (target_scale == 3) converted_temp = fahrenheit_to_kelvin(temperature);
        else converted_temp = temperature;
    } else { // Kelvin
        if (target_scale == 1) converted_temp = kelvin_to_celsius(temperature);
        else if (target_scale == 2) converted_temp = kelvin_to_fahrenheit(temperature);
        else converted_temp = temperature;
    }

    // Display converted temperature
    if (target_scale == 1)
        printf("Converted temperature: %.2f°C\n", converted_temp);
    else if (target_scale == 2)
        printf("Converted temperature: %.2f°F\n", converted_temp);
    else
        printf("Converted temperature: %.2fK\n", converted_temp);

    // Categorize and provide advisory
    categorize_temperature(current_scale == 1 ? temperature : (target_scale == 1 ? converted_temp : kelvin_to_celsius(temperature)));
}

// Conversion functions
float celsius_to_fahrenheit(float celsius) {
    return (celsius * 9 / 5) + 32;
}

float fahrenheit_to_celsius(float fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

float celsius_to_kelvin(float celsius) {
    return celsius + 273.15;
}

float kelvin_to_celsius(float kelvin) {
    return kelvin - 273.15;
}

float fahrenheit_to_kelvin(float fahrenheit) {
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit));
}

float kelvin_to_fahrenheit(float kelvin) {
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin));
}

// Categorization and advisory function
void categorize_temperature(float celsius) {
    if (celsius < 0) {
        printf("Temperature category: Freezing\nWeather advisory: It's freezing. Stay warm!\n");
    } else if (celsius >= 0 && celsius <= 10) {
        printf("Temperature category: Cold\nWeather advisory: Wear a jacket.\n");
    } else if (celsius > 10 && celsius <= 25) {
        printf("Temperature category: Comfortable\nWeather advisory: You should feel comfortable.\n");
    } else if (celsius > 25 && celsius <= 35) {
        printf("Temperature category: Hot\nWeather advisory: Stay hydrated.\n");
    } else {
        printf("Temperature category: Extreme Heat\nWeather advisory: Stay indoors and avoid the heat.\n");
    }
}
