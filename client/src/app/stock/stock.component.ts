import { Component } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { HttpService } from '../http.service';
import { Stock } from '../model';
import { HttpErrorResponse } from '@angular/common/http';
import { take, catchError, throwError } from 'rxjs';


@Component({
  selector: 'app-stock',
  templateUrl: './stock.component.html',
  styleUrls: ['./stock.component.scss']
})
export class StockComponent {
  displayedColumns: string[] = ['name', 'symbol'];
  stock: Stock | null = null
  constructor(private http: HttpService) {}

  public stockForm = new FormGroup({
    filterBar: new FormControl('')
  });

  getStock(): void {
    let requestedStock = this.stockForm.value.filterBar!.toUpperCase();
    this.http.get<Stock[]>(`/api/stocks/${requestedStock}`).pipe(
      take(1),
      catchError((error: HttpErrorResponse) => {
        if (error.status === 400) {
          this.stock = null;
        }
        return throwError(() => new Error(error.message));
      })
    ).subscribe({
      next: (res: Stock) => { this.stock = res},
      error: (error: any) => { console.error('Error:', error) }
  });
  }
}
