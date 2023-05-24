// JavaScript code for seat map

// Function to initialize seat map
function initializeSeatMap() {
  const seatMapElement = document.getElementById('seat-map');

  // Add event listeners for seat selection
  const seatElements = document.querySelectorAll('.seat.available');
  seatElements.forEach(seatElement => {
      seatElement.addEventListener('click', () => {
          seatElement.classList.toggle('selected');
          updateSelectedSeat();
      });
  });
}

// Function to update the selected seat input value
function updateSelectedSeat() {
  const selectedSeats = document.querySelectorAll('.seat.selected');
  const selectedSeatIds = Array.from(selectedSeats).map(seat => seat.dataset.seat);
  document.getElementById('selected-seat').value = selectedSeatIds.join(',');
  document.getElementById('book-btn').disabled = selectedSeatIds.length === 0;
}

// Call the initializeSeatMap function when the page loads
document.addEventListener('DOMContentLoaded', initializeSeatMap);
