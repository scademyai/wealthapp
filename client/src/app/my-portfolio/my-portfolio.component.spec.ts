import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MyPortfolioComponent } from './my-portfolio.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { StockCardComponent } from '../stock-card/stock-card.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { HttpService } from '../http.service';
import { Stock } from '../model';
import { of, throwError } from 'rxjs';

describe('MyPortfolioComponent', () => {
  let component: MyPortfolioComponent;
  let fixture: ComponentFixture<MyPortfolioComponent>;
  let httpService: HttpService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyPortfolioComponent, StockCardComponent],
      imports: [MatGridListModule, HttpClientTestingModule],
      providers: [HttpService],
    });
    fixture = TestBed.createComponent(MyPortfolioComponent);
    component = fixture.componentInstance;
    httpService = TestBed.inject(HttpService);
    fixture.detectChanges();

  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should fetch stocks in portfolio', () => {
    const mockStocks: Stock[] = [
      { quantity: '1', ticker: 'AAPL', price: '100' },
      { quantity: '2', ticker: 'GOOGL', price: '150' }
    ];

    spyOn(httpService, 'get').and.returnValue(of(mockStocks));

    component.getStocks();

    expect(httpService.get).toHaveBeenCalledWith('/api/portfolio/');
    expect(component.stocks.length).toBe(2);
    expect(component.stocks).toEqual(mockStocks);
  });

  it('should set stocks to an empty array when the error status is 400', () => {
    spyOn(httpService, 'get').and.returnValue(throwError({ status: 400 }));

    component.getStocks();

    expect(httpService.get).toHaveBeenCalledWith('/api/portfolio/');
    expect(component.stocks.length).toBe(0);
  });

  it('should handle other error statuses', () => {
    spyOn(console, 'error');
    spyOn(httpService, 'get').and.returnValue(throwError({ status: 500 }));

    component.getStocks();

    expect(httpService.get).toHaveBeenCalledWith('/api/portfolio/');
    expect(console.error).toHaveBeenCalled();
  });

});
