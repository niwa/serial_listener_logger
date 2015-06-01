# Serial Listener and Logger (SeLL)
Simple Python script to listen for messages on a serial port, timestamp every line and save it to a file named by the date.

The settings.txt file gives the required information to the script using the following format:

```
<SERIAL PORT ADDRESS>,<BAUDRATE>,<PARITY>,<BYTESIZE>,<EOL char>
<DATA SAVE PATH>
<short(YYYYMMDD.tsv)/long(YYY-MM-DD.tsv) data filename>,<UTC or local for the timestamp>
<compress data? 1 == YES>
```
The naming of the stored files follows the settings flag short/long.

## Modules required
* **pyserial**
* **time**
* **subprocess**
* **logging**

## License
See [license file](./LICENSE.md)

