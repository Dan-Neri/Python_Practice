"""
Design a system that manages the reservation state of n seats that are 
numbered from 1 to n.

Implement the SeatManager class:

  - SeatManager(int n) Initializes a SeatManager object that will manage
    n seats numbered from 1 to n. All seats are initially available.
  - int reserve() Fetches the smallest-numbered unreserved seat, 
    reserves it, and returns its number.
  - void unreserve(int seatNumber) Unreserves the seat with the given 
    seatNumber.

 

Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve",
 "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a 
SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the 
lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so 
return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available 
seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so 
return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so 
return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return 
the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so 
return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available 
seats are [5].

 

Constraints:

  - 1 <= n <= 105
  - 1 <= seatNumber <= n
  - For each call to reserve, it is guaranteed that there will be at 
    least one unreserved seat.
  - For each call to unreserve, it is guaranteed that seatNumber will be
    reserved.
  - At most 10^5 calls in total will be made to reserve and unreserve.

"""

class SeatManager:
    #Strategy:
        #1. Iniitalize the SeatManager object with an empty list, seats,
            #of size n + 1 in order to align the indices.
        #2. Initialize seats[0] to 'x' to show it is invalid
        #3. When reserve() is called, find the first empty seat using
            #seats.index(None). Mark the seat as reserved and return
            #its index
        #4. When unreserve(seatNumber) is called, set that seat to None

    #Time complextiy: O(N)
    #Space complexity: O(N) 
    def __init__(self, n: int):
        self.seats = [None] * (n + 1)
        self.seats[0] = 'x'

    #Time complextiy: O(N)
    #Space complexity: O(1) 
    def reserve(self) -> int:
        seat = self.seats.index(None)
        self.seats[seat] = 'reserved'
        return seat
        
    #Time complextiy: O(1)
    #Space complexity: O(1) 
    def unreserve(self, seatNumber: int) -> None:
        self.seats[seatNumber] = None
        
import heapq

class HeapSeatManager:
    #Strategy:
        #1. Iniitalize the HeapSeatManager object with a list, seats,
            #containing seatNumbers 1 through n
        #2. Use heapq to convert the list to a heap
        #3. When reserve() is called, pop the root of seats and return
            #it
        #4. When unreserve(seatNumber) is called, push the seatNumber
            #onto seats
    
    #Time complextiy: O(N)
    #Space complexity: O(N)
    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]
        heapq.heapify(self.seats)
        
    #Time complextiy: O(log(N))
    #Space complexity: O(1)
    def reserve(self) -> int:
        return heapq.heappop(self.seats)
        
    #Time complextiy: O(log(N)
    #Space complexity: O(1)
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)

    
if __name__ == "__main__":
    print("Brute force test:")
    test = SeatManager(5)
    print(test.reserve())
    print(test.reserve())
    print(test.unreserve(2))
    print(test.reserve())
    print(test.reserve())
    print(test.reserve())
    print(test.reserve())
    print(test.unreserve(5))
    
    print("Heap Test:")
    hTest = HeapSeatManager(5)
    print(hTest.reserve())
    print(hTest.reserve())
    print(hTest.unreserve(2))
    print(hTest.reserve())
    print(hTest.reserve())
    print(hTest.reserve())
    print(hTest.reserve())
    print(hTest.unreserve(5))