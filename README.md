# Serial Listener and Logger (SeLL)
Simple Python script to listen for messages on a serial port, timestamp every line and save it to a file named by the date.

The settings.txt file gives the required information to the script using the following format:

```
<SERIAL PORT ADDRESS>,<BAUDRATE>,<PARITY>,<BYTESIZE>,<EOL char>
<DATA SAVE PATH>
<compress data? 1 == YES>
```
The naming of the stored files is **YYYY-MM-DD.txt** (e.g., 2015-01-31.txt).

## Modules required
* **pyserial**
* **time**
* **subprocess**

## License
See [license file](./LICENSE.md)

