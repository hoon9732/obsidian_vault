```
cout << ltm->tm_year + 1900 << '-'
     << setfill('0') << setw(2) << ltm->tm_mon + 1 << '-'
     << setfill('0') << setw(2) << ltm->tm_mday << '\n';

```
- `tm_year` is years since 1900 → add 1900.
- `tm_mon` is months since January → add 1.
- `setw(2)` ensures two-digit formatting (e.g., `03` instead of `3`).
- `setfill('0')` pads with `0`.