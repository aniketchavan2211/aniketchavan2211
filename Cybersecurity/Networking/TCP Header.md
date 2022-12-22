### TCP Header

Suppose you want send a file
File is divide into piecies or chunks called as packets.

**each packet/chunks has**:
- data link  header
- IP link Header
- tcp header
- data

**IP header has**:
- source IP (src IP):  from where data is coming from sender
- destination IP (dest IP): to where is data receiving receiver

### TCP

source port: sender port (service: ssh 22, ftp 21, http 80, https 443)
destination port: receiver port number

both sender port and receiver port could be different

sequnece number: random numbers
when Machine A wants to connect Machine B on ssh service port 22 
Machine A need IP Adress port on which Machine B is running and sequence number

acknowledgement number: sequence number + 1 = ACK
used for packet is received and reply with adding 1.


Machine A -> 340(Sequence number) -> Machine B
Machine A <- 340(Sequence number) + 1(ACK number)  <- Machine B

### 3-way Handshake

Machine A -> seq. no. + SYN=1 flag -> Machine B

Machine A <- ack. no.(+1) + ACK=1 flag + SYN=1 + seq. no.   <- Machine B

Machine A ->  ack. no.(+1) + ACK=1 flag  -> Machine B

### header length

size of TCP header

### reserved bits

### urgent flag

URG=1 flag data will set to high priority
before other data blogs sent this data first.
others packet will stop.

### urgent pointer

every blog has address or number, 
urgent pointer store the address.
Machine B will execute will execute blog
that URG flag set to 1.


### PUSH flag

PSH flag = 1 instantly move to buffer
direct to appliaction.

### FIN flag

To terminated connection 

Machine A -> FIN=1 -> Machine B
Machine A <- ACK=1 + FIN=1 <- Machine B
Machine A -> ACk -> Machine B

**open port**
Machine A -> seq. no. + SYN=1 -> Machine B
Machine A <- seq. no. + ack. no.(+1) + SYN=1 + ACK=1 <- Machine B
Machine A -> ACK -> Machine B

**close port**

Machine A -> SYN -> Machine B
Machine A <- ACK=1 + RST=1 <- Machine B

### Windows size

if window size set 5 then 
Machine B wait until Machine A sends 5 SYN packets
and reply with ACK.

### checksums

to check data is modified during transfer.
simply to check integity.

PoH + TCP + Data = checksum

value with packets sent.
receiver passwd through hash function 
compare the output of checksum value match with
now passed packets hash function value.

**PoH: Pseudo header**
- source ip
- destination ip
- zeros
- protocol
- tcp length

