import sys
import logging
import json
from socket import *
HOST = "0.0.0.0"
PORT = 8080

def connect(host, port):
    try:
        connection = socket(AF_INET, SOCK_STREAM)
        connection.connect((host, port))
    except:
        logging.exception("Couldn't connect\n")
        exit(1)

    print("Connected to " + HOST + ':' + str(PORT) + '\n')
    return connection

def createBox(sckt, uuid):
    create_msg = dict()
    create_msg['type'] = "create"
    create_msg['uuid'] = uuid
    try:
        sckt.sendall(json.dumps(create_msg)+'\r\n')
    except:
        logging.exception("Couldn't create the box")
    print("Box created successfully!")

def listBox(sckt, user_id):
    list_msg = dict()
    list_msg['type'] = "list"
    list_msg['id'] = user_id
    try:
        sckt.sendall(json.dumps(list_msg)+'\r\n')
    except:
        logging.exception("Couldn't list the users")

def newBox(sckt, user_id):
    new_msg = dict()
    new_msg['type'] = "new"
    new_msg['id'] = user_id
    try:
        sckt.sendall(json.dumps(new_msg)+'\r\n')
    except:
        logging.exception("Couldn't list the new messages")

def allBox(sckt, user_id):
    all_msg = dict()
    all_msg['type'] = "all"
    all_msg['id'] = user_id
    try:
        sckt.sendall(json.dumps(all_msg)+ '\r\n')
    except:
        logging.exception("Couldn't list all messages")

def sendBox(sckt, src_id, dst_id, msg):
    send_box = dict();
    send_box['type'] = "send"
    send_box['src'] = src_id
    send_box['dst'] = dst_id
    send_box['msg'] = msg
    send_box['copy'] = msg

    try:
        sckt.sendall(json.dumps(send_box)+ '\r\n')
    except:
        logging.exception("Couldn't send message")

def recvBox(sckt, user_id, msg_id):
    recv_box = dict()
    recv_box['type'] = "recv"
    recv_box['id'] = user_id
    recv_box['msg'] = msg_id

    try:
        sckt.sendall(json.dumps(recv_box)+ '\r\n')
    except:
        logging.exception("Couldn't confirm to receive message")

def receiptBox(sckt, user_id, msg_id, receipt): #INCORRET
    receipt_box = dict()
    receipt_box['type'] = "receipt"
    receipt_box['id'] = user_id
    receipt_box['msg'] = msg_id
    receipt_box['receipt'] = receipt

    try:
        sckt.sendall(json.dumps(receipt_box)+ '\r\n')
    except:
        logging.exception("Couldn't confirm to receipt message")

def statusBox(sckt, user_id, msg_id):
    stat_box = dict()
    stat_box['type'] = "status"
    stat_box['id'] = user_id
    stat_box['msg'] = msg_id

    try:
        sckt.sendall(json.dumps(stat_box)+ '\r\n')
    except:
        logging.exception("Couldn't checking the reception status")


def main():
    con = connect(HOST, PORT)
    while True:
        print("1. Create message box\n")
        print("2. List users with a message box\n")
        print("3. List the new messages\n")
        print("4. List all messages\n")
        print("5. Client send a message to a user's message box\n")
        print("6. Client confirm to receive a message from a users message box\n")
        print("7. Receipt messages \n");
        print("8. Checking the reception status of a sent message\n");
        opt = input("Select an option: \n")
        if opt == 1:
            uuid = input("Please insert your ID: ")
            createBox(con, uuid)
        if opt == 2:
            u_id = input("Please insert the id of the user to be listed: ")
            listBox(con, u_id)
        if opt == 3:
            u_id = input("Please insert the id of the user with the new messages: ")
            newBox(con, u_id)
        if opt == 4:
            u_id = input("Please insert the id of the user to list all messages: ")
            allBox(con, u_id)
        if opt == 5:
            u_send = input("Please insert source id of the sender identifier: ")
            u_dst = input("Please insert destination id of the receiver identifier: ")
            u_msg = raw_input("Please insert the message: ")
            sendBox(con, u_send, u_dst, u_msg)
        if opt == 6:
            u_id = input("Please insert the id of the user to confirm the message: ")
            msgid = raw_input("Please insert the message id: ")
            recvBox(con, u_id, msgid)
        if opt == 7:
            u_id = input("Please insert the id of the message box of the receipt sender: ")
            msgid = raw_input("Please insert the identifier of message for which a receipt is being sender: ")
            recpt = raw_input("Please insert msg: ")
            receiptBox(con, u_id, msgid, recpt)
        if opt == 8:
            u_id = input("Please insert the identifier of the receipt box: ")
            msg_id = raw_input("Please insert the message identifier: ")
            statusBox(con, u_id, msg_id)


if __name__ == '__main__':
    main()
