#Code by jeremiah
import network
import usocket as socket
import ussl as ssl
import time

# Function to connect to Wi-Fi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connection with a timeout
    max_wait = 10
    while max_wait > 0:
        if wlan.isconnected():
            print('Connected to Wi-Fi')
            print(wlan.ifconfig())
            return True
        max_wait -= 1
        print('Waiting for connection...')
        time.sleep(1)
    
    print('Connection failed')
    return False

# Function to test download speed
def test_download_speed(url):
    print("Testing download speed...")

    # Record start time
    start_time = time.ticks_ms()

    # Extract host and path from the URL
    _, _, host, path = url.split('/', 3)

    # Connect to the host
    addr = socket.getaddrinfo(host, 443)[0][-1]
    s = socket.socket()
    s.connect(addr)

    # Wrap socket with SSL
    s = ssl.wrap_socket(s)

    # Send the GET request
    s.write(b"GET /%s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n" % (path, host))

    # Receive data
    data = s.read(1024)
    total_data = len(data)
    while data:
        data = s.read(1024)
        total_data += len(data)

    s.close()

    # Calculate elapsed time
    end_time = time.ticks_ms()
    elapsed_time = time.ticks_diff(end_time, start_time) / 1000  # convert to seconds

    # Estimate download speed (Mbps)
    download_speed_mbps = (total_data * 8) / (elapsed_time * 1000000)  # convert bytes to bits and seconds to Mbps

    print("Download Speed: {:.2f} Mbps".format(download_speed_mbps))
    print("Elapsed Time: {:.2f} seconds".format(elapsed_time))

# Replace with your Wi-Fi credentials
ssid = 'T E S L A 4g'
password = '87654321'

# URL to test download speed
test_url = "https://github.com/jerom-physicus/qbit-test/blob/main/index.html"

# Connect to Wi-Fi
if connect_wifi(ssid, password):
    # Perform the speed test continuously every 10 seconds
    while True:
        test_download_speed(test_url)
        time.sleep(1)  # Wait for 10 seconds before the next test
 
