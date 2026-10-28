/* Singly linked list push and print. Build: gcc snippets/linked-list.c */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int value;
    struct Node *next;
} Node;

static Node *push(Node *head, int value) {
    Node *n = malloc(sizeof *n);
    if (!n) return head;
    n->value = value;
    n->next = head;
    return n;
}

int main(void) {
    Node *head = NULL;
    for (int i = 1; i <= 3; i++) head = push(head, i);
    for (Node *n = head; n; n = n->next) printf("%d ", n->value);
    printf("\n");
    while (head) {
        Node *next = head->next;
        free(head);
        head = next;
    }
    return 0;
}
