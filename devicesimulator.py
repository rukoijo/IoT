import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import time
import random

async def main():
    # Fetch the connection string from an environment variable
    conn_str = "HostName=lab.azure-devices.net;DeviceId=test101;SharedAccessKey=P5KXqK/h1jUsY26zlIP1HxdeM0P2EMvH8AIoTMehNGI="
 
    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # Connect the device client.
    await device_client.connect()

    # Send a single message
    messageCounter = 0
    while False:
        msgstr = "Message: " + str(messageCounter) + " --- Temp. " + str(20+ random.randint(1,6))
        print("Sending message...", msgstr)
        await device_client.send_message(msgstr)  #123456789012345 is a message that is being sent ABCDEFGHIJ")
        print("Message successfully sent!")

        # Finally, shut down the client
        time.sleep(5 + random.randint(1,5))
        messageCounter += 1
    await device_client.shutdown()

if __name__ == "__main__":
    asyncio.run(main())