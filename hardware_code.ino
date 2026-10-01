#include "DHT.h"

#define PIR_PIN 27
#define LDR_PIN 34
#define DHT_PIN 4
#define LED_PIN 5

#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {

  Serial.begin(115200);

  pinMode(PIR_PIN, INPUT);
  pinMode(LDR_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  digitalWrite(LED_PIN, LOW);

  dht.begin();

  delay(30000);   // PIR warm-up

  Serial.println("ASTRA_GRID_READY");

}

void loop() {

  int pirValue = digitalRead(PIR_PIN);
  int ldrValue = analogRead(LDR_PIN);

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();


  // -----------------------------
  // LIGHTING DECISION
  // -----------------------------

  bool lighting = false;

  if (pirValue == HIGH && ldrValue < 1000) {

    lighting = true;
    digitalWrite(LED_PIN, HIGH);

  }

  else {

    lighting = false;
    digitalWrite(LED_PIN, LOW);

  }


  // -----------------------------
  // COOLING DECISION
  // -----------------------------

  bool cooling = false;

  if (!isnan(temperature) && temperature >= 30.0) {

    cooling = true;

  }


  // -----------------------------
  // SEND DATA TO PYTHON
  // -----------------------------

  if (!isnan(temperature) && !isnan(humidity)) {

    Serial.print(pirValue);
    Serial.print(",");

    Serial.print(ldrValue);
    Serial.print(",");

    Serial.print(temperature, 1);
    Serial.print(",");

    Serial.print(humidity, 1);
    Serial.print(",");

    Serial.print(lighting ? 1 : 0);
    Serial.print(",");

    Serial.println(cooling ? 1 : 0);

  }


  delay(2000);

}