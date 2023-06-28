import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Stock } from '../model';
import { HttpService } from '../http.service';
import { take } from 'rxjs';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.scss']
})
export class StocksComponent {
  constructor(private http: HttpService
  ) {}

  
  stocks: Stock[] = [
    {
      "ticker": "TSLA",
      "price": "270.00",
      "volume": "1000000"
  },
  {
      "ticker": "AAPL",
      "price": "200.00",
      "volume": "2000000"
  },
  {
      "ticker": "GOOG",
      "price": "1000.00",
      "volume": "3000000"
  }
];

  public stockForm = new FormGroup({
    filterBar: new FormControl('')
  });

  getStocks() {
    let searchedStocks = this.arrayOfStocksSeperatedByComma();

    this.http.post('/api/stocks/', {"symbols": searchedStocks}).pipe(take(1)).subscribe((res) => {
      if(Array.isArray(res)) {
        this.stocks = res;
      }
      else {
        this.stocks = [res as Stock];
      }
    });
  }

  arrayOfStocksSeperatedByComma() {
    var arrayOfStocks = [];
    var currentStock = "";
    console.log(this.stockForm.value.filterBar);
    if(this.stockForm.value.filterBar) {
      for (var i = 0; i < this.stockForm.value.filterBar?.length; i++) {
        if(this.stockForm.value.filterBar[i] === ',') {
          arrayOfStocks.push(currentStock);
          currentStock = "";
        }
        else {
          currentStock += this.stockForm.value.filterBar?.toUpperCase()[i];
        }
      }
      arrayOfStocks.push(currentStock);
    }
    return arrayOfStocks;
  }
}
