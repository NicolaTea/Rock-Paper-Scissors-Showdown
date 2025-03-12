<?php
$host = 'X.X.X.X'; //ip
$port = 12345;

// Create a TCP socket
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if (!$socket) {
    die("Eroare la crearea socket-ului: " . socket_strerror(socket_last_error()) . "\n");
}

// Connect to the server
if (!socket_connect($socket, $host, $port)) {
    die("Eroare la conectare: " . socket_strerror(socket_last_error()) . "\n");
}

echo "Te-ai conectat ca Client 1. Asteptam conectarea clientului UDP...\n";

// Read messages from the serve
while ($msg = socket_read($socket, 2048, PHP_NORMAL_READ)) {
    echo $msg;

    // If the choice is requested
    if (strpos($msg, 'Introdu alegerea ta') !== false) {
        $choice = readline();
        socket_write($socket, $choice, strlen($choice));
    }

    // Check if the game has ended
    if (strpos($msg, 'Final:') !== false) {
        break;
    }
}

// Close the socket
socket_close($socket);
?>
