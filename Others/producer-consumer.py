# -------- Semaphore -------------

# wait(S){
# while(S<=0);   // busy waiting
# S--;
# }

# signal(S){
# S++;
# }


# --------------- Producer ------------

# do{

# //produce an item

# wait(empty); supposed to produce to fill up the empty, so add to the empty
# wait(mutex); wait for the mutex

# //place in buffer

# signal(mutex);
# signal(full);

# }while(true)


# --------------- Consumer ------------
# do{

# wait(full); supposed to consume from the full, so minus the full
# wait(mutex); wait for the mutex

# // remove item from buffer

# signal(mutex);
# signal(empty);

# // consumes item

# }while(true)


# ------------ wrong code -----------


# ------------- producer ------------
# while (true) {
#     while(counter == BUFFER SIZE); do nothing

#     buf[in] = produced;
#     in = (in + 1) % BUFFER SIZE
#     counter++;
# }


# ----------- consumer -------------
# while (true) {
#     while(counter == 0); do nothing

#     consumed = buf[out];
#     out = (out + 1) % BUFFER SIZE
#     counter++;
# }