#include <RH_ASK.h>
#include <SPI.h> // Not actualy used but needed to compile
 
RH_ASK driver;
 
struct dataStruct{
  float final_val;
  int load_id[16];
}myData;
void setup()
{
    Serial.begin(9600); // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}
 
void loop()
{
    uint8_t buf[RH_ASK_MAX_MESSAGE_LEN];   //RH_ASK_MAX_MESSAGE_LEN is the maximum rf packet length. uint8_t is the same as a byte. its shorthand for: a type of unsigned integer of length 8 bits
    uint8_t buflen = sizeof(buf);          //This gives length of the message/array
    if (driver.recv(buf, &buflen)) // Non-blocking
    {
      int i;
      //driver.printBuffer("Got: ", buf, buflen);
      memcpy(&myData, buf, sizeof(myData));  //translates rf signal from buf into myData
      // Message with a good checksum received, dump it.
      Serial.print("W:");
      Serial.println(myData.final_val);
      Serial.print("ID:");
      for(int i = 0; i < 16; i++){
        Serial.print(myData.load_id[i]);
      }
     Serial.println();     
    }
 
}
