import Parser
import threading

WALLET_URL = "https://solscan.io/account/Hnnw2hAgPgGiFKouRWvM3fSk3HnYgRv4Xq1PjUEBEuWM#solTransfers"
BOT_API_TOKEN = "заглушка"


#Parser.getLastOperationInfo(WALLET_URL, "ЗАГЛУШКА")
frst_thread = threading.Thread(target=Parser.getLastOperationUrl('https://solscan.io/account/9nrRN7pBM3Fdtm3wEHaTbf9adhMyBhPEAQHXBRdDzVxa'))
scnd_thread = threading.Thread(target=Parser.getLastOperationUrl('https://solscan.io/account/H3BuxR5wD5ac6m1G9G7zbhibg3jqX73vcMWiRYN4VhCX'))

#Parser.getLastOperationUrl('https://solscan.io/tx/5VER3zahe1XggtGHRa31G8VUQ755NXTn1s4phyc6Wpf99pGaksfvc1j6mF9nP5TzLJ6Xg1x4MNWoZ1ML5k4jrkmZ')
#Parser.getLastOperationUrl('https://solscan.io/tx/5VER3zahe1XggtGHRa31G8VUQ755NXTn1s4phyc6Wpf99pGaksfvc1j6mF9nP5TzLJ6Xg1x4MNWoZ1ML5k4jrkmZ')
#Parser.getLastOperationUrl('https://solscan.io/tx/5zPJ9a3uvTuwamtsso8mQHUvnaVT5K5JE9yZ9SnLNMJTP6dc8fpcuZL16PqZfTLxtRrimyjC4iKG15Zm1uwXLSTB')
#Parser.getLastOperationUrl('https://solscan.io/tx/5VER3zahe1XggtGHRa31G8VUQ755NXTn1s4phyc6Wpf99pGaksfvc1j6mF9nP5TzLJ6Xg1x4MNWoZ1ML5k4jrkmZ')
