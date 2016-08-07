public class ReservationSystem{
 final Map<integer room=""> rooms;
 Map<string customer=""> customers;

 public ReservationSystem(List<room> builtRoom){
  rooms = new HashMap<integer room=""> ();
  //when the hotel is built, all the rooms are added into the system
  rooms.add(builtRoom);
  customers = new HashMap<string customer=""> ();
 }

 public boolean makeReservation(String name, String id, String information){
  int room = findNextAvailableRoom();
  if(room == -1){
   System.out.println("No available room!");
   return false;
  }
  Customer c = new Customer(name, id, information, room);
  rooms.get(room).book();
  customers.put(name, c);
  return true;
 }

 public boolean cancelReservation(String name){
  Customer c = findCustomer(name);
  if(c == null){
   System.out.println("No reservation found!");
   return false;
  }
  customers.remove(name);
  makeAvailable(c.roomBooked);
  return true;
 }

 private Customer findCustomer(String name){
  if(!customers.containsKey(name))
   return null;
  return customers.get(name);
 }

 private void makeAvailable(int roomNumber){
  rooms.get(roomNumber).unbook();
 }
 private int findNextAvailableRoom(){
  for(Room r : rooms.values()){
   if(!r.isBooked())
    return r.roomNumber;
  }
  return -1;
 }


 class Room{
  final int roomNumber;
  private boolean available;

  public Room(int rN){
   roomNumber = rN;
   available = true;
  }

  public void book(){
   available = false;
  }
  void unbook(){
   available = true;
  }
  public boolean isBooked(){
   return !available;
  }
 }

 class Customer{
  String name;
  String id;
  String information;
  int roomBooked;

  public Customer(String name, String id, String information, int roomNumber){
   this.name = name;
   this.id = id;
   this.information = information;
   roomBooked = roomNumber;
  }
 }