Project Name: 
      Programming Assignment 1

Project Description:
      Implementing FTP server and FTP client, where the client connects to the 
      server and supports uploading and downloading of files to/from server. 

Names and emails of all partners in the group (Name - Email):
      James Pham - jpham25@csu.fullerton.edu
      Kelton Benson - kelton01@csu.fullerton.edu
      Phuoc Nguyen - phuocnguyen102800@csu.fullerton.edu
      Arturo Salazar - arturosi1@csu.fullerton.edu
      Kingston Leung - leungkingston@csu.fullerton.edu

Programming Language:
      We are using Python to develop this programming project. 

To execute this program:
      Server:
	  invoke server process as "serv.py <port number>"
	  Server will now await for client connections.
		- Port 5001 is reserved for data transfer sockets. Please avoid initializing
		  server on this port.

      Client:
	  invoke client process as "cli.py localhost <port number>"
		- Client will only work on "localhost" address.
		- <port number> should match server's port number.
      Upon connecting to the server, the client prints out ftp>, which allows the user to execute the
      following commands:
            ftp> get <file name> (downloads file <file name> from the server)
            ftp> put <file name> (uploads file <file name> to the server)
            ftp> ls (lists files on theserver)
            ftp> quit (Closes client connection. Server will wait for a new connection)

Special Notes to take:
      We used pickle from Python which is a module that implements binary 
      protocols for serializing and de-serializing a Python object structure,
      which keeps track of the objects that are serialized, so that later references 
      to the same object won't be serialized again. This helps us avoid data loss when sending
      our commands back and forth between the server and client.