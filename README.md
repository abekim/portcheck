Portcheck API
============

A simple JSON API for checking if port is open at a specified host. 

&copy; Copyright DiViS DVR &trade; 2014

Methods
-----------

#### `/<host>/<port>`
Returns a JSON object indicating whether `port` is open at `host`.

```javascript
{
  "data": "google.com:80 is open"
}
```
