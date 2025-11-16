# ALX Travel App - Milestone 2
*Model, Serializers & Database Seeding*

## Project Overview
This milestone focuses on building essential backend components for the `alx_travel_app_0x00` project.
Learners will define relational database models, build serializers for API data exchange, and create a custom Django management command to seed the database with realistic sample data. This milestone replicates real-world backend development workflows used in travel-booking platforms.

## Learning Objectives
By completing this milestone, you will be able to:
- Design and implement relational models using Django ORM
- Apply ForeignKey and one-to-many relationships correctly
- Build Django REST Framework (DRF) serializers for converting models to JSON
- Create a database seeding management command
- Automate population of sample listings, bookings, and reviews
- Validate your work using Django CLI tools

## Models Implemented
All models are located in:
```bash
alx_travel_app/listings/models.py
```
#### 1. Listing Model
Represent properties available for booking in the travel platform. Includes metadata like name, price, location, and availability.

#### 2. Booking Model
Represents a customer's reservation of listing. Linked to the `Listing` model via `ForeignKey`.

#### 3. Review Model
Tracks customer ratings and comments for a listing.

#### Key Relationships
- `Listing` → `Booking`: One-to-many
- `Listing` → `Review`: One-to-many
- Foreign keys include constraints to ensure data consistency.

## Serializers
Serializers are defined in:
```bash
alx_travel_app/listings/serializers.py
```
#### Implemented Serializers:
- `ListingSerializer`
- `BookingSerializer`
These serializers convert model instance into JSON for API responses and validate incoming request data.

## Database Seeder
The milestone include a custom Django management command to populate the database with realistic test data.

Location:
```bash
alx_travel_app/listings/management/commands/seed.py
```
The seeder:
- Generate multiple listings
- Optionally creates bookings and reviews
- Helps testers and frontend developers work with real-looking data without manual entry

### How to Run the Seeder
Run the following command from the project root:
```bash
python manage.py seed
```
You should see output indicating that listings have been created.

## Project Structure
```bash
alx_travel_app_0x00/
 └── alx_travel_app/
      ├── listings/
      │    ├── models.py
      │    ├── serializers.py
      │    └── management/
      │         └── commands/
      │              └── seed.py
      ├── settings.py
      └── ...
```
## Testing
- Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
- Run the seeder:
```bash
python manage.py seed
```
- Inspect the database:
```bash
python manage.py shell
```
- Test endpoints
```bash
/api/listings/
/api/bookings/
```
## Real-World User Case
in travel platform like Airbnb, Booking.com, or TravelPerk:
- Listings represent properties
- Bookings connect customers to listings
- Reviews improve trust and feedback loops
- Serializers expose the data to apps and frontends
- Seed data speeds up development by giving the team realistic, stable test data
This milestone simulates exactly how modern backend teams bootstrap data during development.