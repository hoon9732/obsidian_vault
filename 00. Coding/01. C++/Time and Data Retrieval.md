```
time_t now = time(0);
tm *ltm = localtime(&now);

```
- `time(0)` gets the current time in seconds since the Unix epoch (Jan 1, 1970).
- `localtime(&now)` converts it into a `tm` structure representing the local time.