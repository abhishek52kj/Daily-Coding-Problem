#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

int length(ListNode* head) {
    int count = 0;
    while (head) {
        count++;
        head = head->next;
    }
    return count;
}

ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
    int lenA = length(headA);
    int lenB = length(headB);

    while (lenA > lenB) {
        headA = headA->next;
        lenA--;
    }

    while (lenB > lenA) {
        headB = headB->next;
        lenB--;
    }

    while (headA != headB) {
        headA = headA->next;
        headB = headB->next;
    }

    return headA;
}

// Function to print the linked list
void printList(ListNode* head) {
    while (head) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    // Example linked lists
    ListNode* A = new ListNode(3);
    A->next = new ListNode(7);
    A->next->next = new ListNode(8);
    A->next->next->next = new ListNode(10);

    ListNode* B = new ListNode(99);
    B->next = new ListNode(1);
    B->next->next = A->next->next;  // Connecting the lists at node with value 8

    // Finding the intersecting node
    ListNode* result = getIntersectionNode(A, B);

    // Output the result
    if (result) {
        cout << "Intersecting node value: " << result->val << endl;
    } else {
        cout << "No intersection found." << endl;
    }

    // Deallocate memory
    delete A->next->next;  // Deleting the common node to avoid memory leaks
    delete A;
    delete B->next;
    delete B;

    return 0;
}
