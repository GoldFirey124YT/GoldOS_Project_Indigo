using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace Server
{
    class Program
    {
        private static readonly Socket _serverSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        private static readonly byte[] _buffer = new byte[1024];
        private static readonly List<Socket> _clientSockets = new List<Socket>();
        private static readonly ManualResetEvent _allDone = new ManualResetEvent(false);

        static void Main(string[] args)
        {
            SetupServer();
        }

        private static void SetupServer()
        {
            Console.WriteLine("Setting up server...");
            _serverSocket.Bind(new IPEndPoint(IPAddress.Any, 3333));
            _serverSocket.Listen(5);
            _serverSocket.BeginAccept(AcceptCallback, null);
            Console.WriteLine("Server setup complete!");
        }

        private static void AcceptCallback(IAsyncResult ar)
        {
            _allDone.Set();
            Socket socket = _serverSocket.EndAccept(ar);
            _clientSockets.Add(socket);
            socket.BeginReceive(_buffer, 0, _buffer.Length, SocketFlags.None, ReceiveCallback, socket);
            Console.WriteLine("Client connected.");
            _serverSocket.BeginAccept(AcceptCallback, null);
        }

        private static void ReceiveCallback(IAsyncResult ar)
        {
            Socket socket = (Socket)ar.AsyncState;
            int bytesRead = socket.EndReceive(ar);

            byte[] dataBuffer = new byte[bytesRead];
            Array.Copy(_buffer, dataBuffer, bytesRead);

            string text = Encoding.ASCII.GetString(dataBuffer);
            Console.WriteLine("Message received: " + text);

            foreach (Socket clientSocket in _clientSockets)
            {
                if (clientSocket != socket)
                {
                    clientSocket.Send(dataBuffer);
                }
            }

            socket.BeginReceive(_buffer, 0, _buffer.Length, SocketFlags.None, ReceiveCallback, socket);
        }
    }
}
