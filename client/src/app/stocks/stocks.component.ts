import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Stock } from '../model';
import { HttpService } from '../http.service';
import { catchError } from 'rxjs/operators';
import { throwError, take } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-stocks',
  templateUrl: './stocks.component.html',
  styleUrls: ['./stocks.component.scss']
})
export class StocksComponent implements OnInit{
  constructor(private http: HttpService
  ) {}

  ngOnInit(): void {
    this.getStocks();
  }

  stocks: Stock[] = [];

  public stockForm = new FormGroup({
    filterBar: new FormControl('')
  });

  getStocks(): void {
    let searchedStocks = this.extractStockSymbols();

    this.http.get<Stock[]>(`/api/stocks/?symbols=${searchedStocks}`).pipe(
      take(1),
      catchError((error: HttpErrorResponse) => {
        if (error.status === 400) {
          this.stocks = [];
        }
        return throwError(() => new Error(error.message));
      })
    ).subscribe({
      next: (res: Stock[] | Stock) => {
        if (Array.isArray(res)) {
          this.stocks = res;
        } else {
          this.stocks = [res as Stock];
        }
      },
      error: (error: any) => { console.error('Error:', error) }
    });
  }

  extractStockSymbols(): string[] {
    if (!this.stockForm.value.filterBar) {
      return [];
    }

    const searchBarValue = this.stockForm.value.filterBar.toUpperCase();
    return searchBarValue.split(',').map((symbol: string) => symbol.trim());
  }
}
