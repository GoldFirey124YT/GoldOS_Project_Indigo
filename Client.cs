using System;
using System.Net.Sockets;
using System.Text;
using System.Windows.Forms;

namespace Project Indigo
{
    public partial class Form1 : Form
    {
        private readonly Socket _clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        private readonly byte[] _buffer = new byte[1024];

        public Form1()
        {
            InitializeComponent();
        }

        private void ConnectButton_Click(object sender, EventArgs e)
        {
            _clientSocket.Connect(IPAddress.Parse("127.0.0.1"), 3333);
            MessageBox.Show("Connected to server.");
            _clientSocket.BeginReceive(_buffer, 0, _buffer.Length, SocketFlags.None, ReceiveCallback, null);
        }

       
