#!/usr/bin/python

# https://po.kattis.com/problems/vandrarhem


class Bed(object):
    def __init__(self, price, available_beds):
        """ Constructor for Bed """
        self.price = int(price)
        self.available_beds = int(available_beds)

    def is_full(self):
        """ Checks if there is a bed of this type available """
        return self.available_beds == 0

    def book(self):
        """ Books a bed of this type """
        if not self.is_full():
            self.available_beds -= 1


def main():
    with open("infile.txt") as f:
        infile = f.read().splitlines()

    firstline = infile.pop(0)
    attendees = int(firstline.split(" ")[0])
    bedtype_count = int(firstline.split(" ")[1])

    # The total cost for booking a bed for every attendee
    total_cost = 0
    bedtypes = []

    for i in range(bedtype_count):
        line = infile[i]
        tokens = line.split(" ")
        price = tokens[0]
        available = tokens[1]
        bedtypes.append(Bed(price, available))

    # Sort the bedtypes by their price
    bedtypes.sort(key=lambda bed: bed.price)

    bed_type_counter = 0
    # Book a bed for every attendee
    while attendees > 0:
        current_bed_type = bedtypes[bed_type_counter]
        current_bed_price = current_bed_type.price

        if current_bed_type.available_beds == 0:
            bed_type_counter += 1
            continue
        else:
            current_bed_type.book()
            total_cost += current_bed_price
            attendees -= 1

    print(total_cost)

if __name__ == '__main__':
    main()
