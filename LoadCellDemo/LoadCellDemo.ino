#include "HX711.h"
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
#include <avr/boot.h>

RH_ASK driver;

HX711 cell(3, 2);

struct dataStruct{
  float final_val ; 
  int load_id[16];
}myData;

long val = 0;
float count =0;
char my_msg[25];
byte tx_buf[sizeof(myData)] = {0};

void setup() {
  Serial.begin(9600);
  if (!driver.init())
         Serial.println("init failed");
  myData.final_val = 0;
  for( int i=0; i<16; i++){
  int x = boot_signature_byte_get( i);
  myData.load_id[i] = x;
  //Serial.print(x);
  }
}


void loop() {
  count = count+1;
  //val = ((count-1)/count)*val + (1/count)*cell.read();
  //val = cell.read();
  for(int i = 0; i < 30; i++){
    val = 0.5 * val + 0.5 * cell.read();
    myData.final_val = (val - 8387131) / 15168.0f * 192;
    if(myData.final_val < 0){delay(3000);}
  }
  //Serial.println( (val - 8368648)/70388.0f * 892 ); Cell1
  //dtostrf(final_val, 10, 1, my_msg);
  //Serial.println( (val - 8304429)/21583.0f * 128 );
  memcpy(tx_buf, &myData, sizeof(myData));
  byte zize = sizeof(myData);

  Serial.println(myData.final_val);
  // zero 8368648
  if(myData.final_val > 0){
  driver.send((uint8_t *)tx_buf, zize);
  driver.waitPacketSent();
  delay(3131);
  }
}


