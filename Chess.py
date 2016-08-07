class Piece(object):
    def __init__(self, name):
        self.name = name  # name of piece
  
    def set_movement_behavior(self, movementBehavior):
        raise NotImplementedError


class MovementBehavior(object):
    def __init__(self):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError


class SingleForwardMovement(MovementBehavior):
    def __init__(self):
        print "Initialized single forward movement"
   
    def move(self, name):
        print "{} Moving forward by one step".format(name)


class King(Piece):
    def __init__(self, name):
        super(King, self).__init__(name)
        self.set_movement_behavior(SingleForwardMovement())

    def set_movement_behavior(self, movementBehavior):
        self.movementBehavior = movementBehavior
    
    def play(self):
        if not self.movementBehavior:
            self.movementBehavior = SingleForwardMovement()
        self.movementBehavior.move(self.name)


if __name__ == "__main__":
    king = King("king")
    king.play()